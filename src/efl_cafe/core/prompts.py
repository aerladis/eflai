"""
Prompts and parsing utilities.
"""
import os
import re
from configparser import ConfigParser
from datetime import datetime
from ..utils import debug
from .config import APP_VERSION


DEFAULT_PROMPTS = {
    "batch": (
        "You are an ESL materials writer for an online {modifier}{unit_level} discussion class.\n"
        "UNIT: {unit_title}\nCONTENT TOPICS:\n{topics}\nTARGET VOCABULARY (optional): {vocab}\n"
        "CEFR TIER: {cefr_tier}\n\n"
        "RULES\n- EXACTLY 15 questions, numbered 1–15, one per line.\n"
        "- Each is ONE sentence, 12–20 words, ends with '?'.\n"
        "- Use the topics; distribute evenly; high-frequency English, CEFR {unit_level}.\n"
        "- {tier_instructions}\n"
        "- Avoid clichés/filler (amazing/awesome/etc.).\n"
        "OUTPUT: only the 15 numbered questions."
    ),
    "single": (
        "You are an ESL materials writer for an online {modifier}{unit_level} discussion class.\n"
        "UNIT: {unit_title}\nCONTENT TOPICS:\n{topics}\nTARGET VOCABULARY (optional): {vocab}\n"
        "CEFR TIER: {cefr_tier}\n\n"
        "TASK: Write ONE NEW question (12–20 words, one sentence, ends with '?').\n"
        "- {tier_instructions}\n"
        "Avoid clichés. Do not repeat any of these:\n{existing_questions}\n"
        "OUTPUT: only the question text."
    ),
}


def load_prompts(path):
    """Load prompts from configuration file."""
    cfg = ConfigParser()
    if os.path.exists(path):
        try:
            cfg.read(path, encoding="utf-8")
        except Exception:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                cfg.read_file(f)
    
    # Check version compatibility in debug mode
    if debug.DEBUG_MODE:
        check_prompts_version(path)
    
    def get(sec, default): 
        return cfg.get(sec, "template", fallback=default) if cfg.has_section(sec) else default
    
    return {
        "batch": get("batch", DEFAULT_PROMPTS["batch"]),
        "single": get("single", DEFAULT_PROMPTS["single"])
    }


def check_prompts_version(prompts_path):
    """Check if prompts.ini version matches the application version in debug mode."""
    if not os.path.exists(prompts_path):
        debug.debug_print(f"[DEBUG] WARNING: prompts.ini not found at {prompts_path}")
        return
    
    try:
        with open(prompts_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Extract version from the file header
        version_match = re.search(r'# Version:\s*([^\n]+)', content)
        if version_match:
            file_version = version_match.group(1).strip()
            if file_version != APP_VERSION:
                debug.debug_print(f"[DEBUG] ⚠️  VERSION MISMATCH WARNING:")
                debug.debug_print(f"[DEBUG]    Application Version: {APP_VERSION}")
                debug.debug_print(f"[DEBUG]    Prompts File Version: {file_version}")
                debug.debug_print(f"[DEBUG]    File Path: {prompts_path}")
                debug.debug_print(f"[DEBUG]    Please update your prompts.ini file to match the application version.")
                debug.debug_print(f"[DEBUG]    This may cause unexpected behavior or errors.")
                
                # Offer to auto-update the version
                try:
                    update_prompts_version(prompts_path, content)
                except Exception as e:
                    debug.debug_print(f"[DEBUG]    Failed to auto-update version: {e}")
            else:
                debug.debug_print(f"[DEBUG] ✅ Prompts version check passed: {file_version}")
        else:
            debug.debug_print(f"[DEBUG] ⚠️  WARNING: No version information found in prompts.ini")
            debug.debug_print(f"[DEBUG]    Expected version: {APP_VERSION}")
            debug.debug_print(f"[DEBUG]    File: {prompts_path}")
    except Exception as e:
        debug.debug_print(f"[DEBUG] ⚠️  Error checking prompts version: {e}")


def get_prompts_version(prompts_ini_path):
    """Get the version from prompts.ini file."""
    try:
        if os.path.exists(prompts_ini_path):
            with open(prompts_ini_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            version_match = re.search(r'# Version:\s*([^\n]+)', content)
            if version_match:
                return version_match.group(1).strip()
    except Exception:
        pass
    return None


def update_prompts_version(prompts_path, content):
    """Auto-update the version in prompts.ini to match the application version."""
    try:
        # Create a backup of the original file
        backup_path = prompts_path + ".backup"
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(content)
        debug.debug_print(f"[DEBUG] 📁 Created backup: {backup_path}")
        
        # Update the version line
        updated_content = re.sub(
            r'# Version:\s*[^\n]+',
            f'# Version: {APP_VERSION}',
            content
        )
        
        # Update the last updated date
        current_date = datetime.now().strftime("%Y-%m-%d")
        updated_content = re.sub(
            r'# Last Updated:\s*[^\n]+',
            f'# Last Updated: {current_date}',
            updated_content
        )
        
        # Write the updated content back to the file
        with open(prompts_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        
        debug.debug_print(f"[DEBUG] ✅ Auto-updated prompts.ini version to {APP_VERSION}")
        debug.debug_print(f"[DEBUG]    Backup saved as: {backup_path}")
        
    except Exception as e:
        debug.debug_print(f"[DEBUG] ❌ Failed to auto-update prompts.ini: {e}")
        raise


def fmt(t, **kw):
    """Format template string with keyword arguments."""
    try: 
        result = t.format(**kw)
        return result
    except Exception as e:
        debug.debug_print(f"ERROR: Prompt formatting failed: {e}")
        debug.debug_print(f"Template: {t[:200]}...")
        debug.debug_print(f"Available keys: {list(kw.keys())}")
        return t


def get_tier_instructions(level, tier):
    """Generate specific instructions based on CEFR level and tier."""
    if tier == "Lower":
        if level in ["A1", "A2"]:
            return "Use simple present tense, basic vocabulary, and straightforward questions like 'Do you...?', 'Can you...?', 'Do you like...?'"
        elif level in ["B1", "B1+"]:
            return "Use simple to intermediate structures, common vocabulary, and questions like 'Do you think...?', 'Have you ever...?', 'Would you like to...?'"
        else:  # B2, C1, C2
            return "Use intermediate structures, avoid overly complex grammar, and focus on practical, everyday questions"
    elif tier == "Neutral":
        if level in ["A1", "A2"]:
            return "Use appropriate structures for the level, mix of present and past tense, and balanced questions that are neither too simple nor too complex"
        elif level in ["B1", "B1+"]:
            return "Use intermediate structures, standard vocabulary, and well-balanced questions that match the level expectations"
        else:  # B2, C1, C2
            return "Use level-appropriate structures, standard vocabulary, and questions that are challenging but not overly complex"
    else:  # Upper
        if level in ["A1", "A2"]:
            return "Use more varied structures within the level, include past tense, and create engaging questions beyond basic patterns"
        elif level in ["B1", "B1+"]:
            return "Use intermediate to upper-intermediate structures, more sophisticated vocabulary, and thought-provoking questions"
        else:  # B2, C1, C2
            return "Use advanced structures, complex vocabulary, and challenging questions that require critical thinking and detailed responses"


def get_quality_validation_instructions(enabled):
    """Generate quality validation instructions."""
    if not enabled:
        return ""
    return """QUALITY VALIDATION REQUIREMENTS
	- Ensure each question is crystal clear and unambiguous
	- Use perfect grammar and natural phrasing throughout
	- Avoid culturally insensitive or potentially offensive content
	- Make sure questions are appropriate for the target level
	- Double-check that questions sound like natural English"""


def get_blooms_taxonomy_instructions(level, blooms_level):
    """Generate Bloom's taxonomy instructions."""
    if blooms_level == "Auto":
        return ""
    
    instructions = f"BLOOM'S TAXONOMY LEVEL: {blooms_level.upper()}\n"
    
    if blooms_level == "Remember":
        instructions += """	- Focus on factual recall questions
	- Use stems like: What is...?, Who...?, When...?, Where...?, Which...?
	- Ask for basic information and definitions"""
    elif blooms_level == "Understand":
        instructions += """	- Focus on comprehension and explanation
	- Use stems like: Explain why...?, Describe...?, What does... mean?
	- Ask students to interpret or summarize information"""
    elif blooms_level == "Apply":
        instructions += """	- Focus on practical application
	- Use stems like: How would you use...?, Solve...?, What would happen if...?
	- Ask students to use knowledge in new situations"""
    elif blooms_level == "Analyze":
        instructions += """	- Focus on breaking down and comparing
	- Use stems like: Compare...?, What are the differences...?, Why do you think...?
	- Ask students to examine relationships and patterns"""
    elif blooms_level == "Evaluate":
        instructions += """	- Focus on judgment and opinion
	- Use stems like: Do you agree...?, What is your opinion...?, Which is better...?
	- Ask students to make judgments and justify their choices"""
    elif blooms_level == "Create":
        instructions += """	- Focus on original thinking and creation
	- Use stems like: Design...?, Create...?, What if you could...?
	- Ask students to generate new ideas and solutions"""
    
    return instructions


def get_engagement_level_instructions(engagement_level):
    """Generate engagement level instructions."""
    if engagement_level == "Auto":
        return ""
    
    instructions = f"ENGAGEMENT LEVEL: {engagement_level.upper()}\n"
    
    if engagement_level == "Low":
        instructions += """	- Focus on simple, direct questions
	- Use basic vocabulary and straightforward language
	- Keep questions short and easy to understand
	- Avoid complex concepts or abstract thinking"""
    elif engagement_level == "Medium":
        instructions += """	- Use moderate complexity in questions
	- Include some thought-provoking elements
	- Balance simple and more challenging questions
	- Encourage some personal reflection"""
    elif engagement_level == "High":
        instructions += """	- Create engaging, interactive questions
	- Use dynamic language and interesting scenarios
	- Include questions that spark discussion
	- Encourage creative thinking and personal opinions"""
    
    return instructions


def get_academic_background_instructions(enabled):
    """Generate academic background instructions."""
    if not enabled:
        return ""
    return """ACADEMIC BACKGROUND CONSIDERATIONS
	- Assume students have some academic experience
	- Use appropriate academic vocabulary when relevant
	- Include questions that relate to educational contexts
	- Consider formal vs. informal language appropriately"""


def get_naturalness_instructions(enabled):
    """Generate naturalness instructions."""
    if not enabled:
        return ""
    return """NATURALNESS REQUIREMENTS
	- Write questions that sound like natural, conversational English
	- Avoid overly formal or stilted language
	- Use contractions and natural speech patterns when appropriate
	- Make questions feel like they could be asked in a real conversation"""


def get_strictness_instructions(strictness):
    """Generate strictness instructions."""
    if strictness == "Auto":
        return ""
    
    instructions = f"STRICTNESS LEVEL: {strictness.upper()}\n"
    
    if strictness == "Lenient":
        instructions += """	- Allow some flexibility in question structure
	- Accept variations in wording and style
	- Focus on meaning over perfect grammar
	- Be more forgiving with minor errors"""
    elif strictness == "Moderate":
        instructions += """	- Maintain good grammar and structure
	- Ensure questions are clear and well-formed
	- Balance flexibility with quality standards
	- Allow some natural variation"""
    elif strictness == "Strict":
        instructions += """	- Maintain perfect grammar and structure
	- Ensure all questions meet high quality standards
	- Be precise and exact in wording
	- Minimize any variations or errors"""
    
    return instructions


def parse_numbered_questions(text, max_items=15):
    """Parse numbered questions from text."""
    questions = []
    lines = text.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for numbered questions (1., 2., etc.)
        match = re.match(r'^\d+\.\s*(.+)$', line)
        if match:
            question = match.group(1).strip()
            if question and question.endswith('?'):
                questions.append(question)
        
        # Stop if we have enough questions
        if len(questions) >= max_items:
            break
    
    return questions
