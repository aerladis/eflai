"""
DPI awareness and display utilities.
"""
import os


def _enable_win_per_monitor_dpi_awareness():
    """Enable Windows per-monitor DPI awareness."""
    if os.name != "nt":
        return
    import ctypes
    try:
        # Windows 10+ : Per-Monitor-V2 (best)
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))  # PER_MONITOR_AWARE_V2
        return
    except Exception:
        pass
    try:
        # Windows 8.1 : Per-Monitor (fallback)
        PROCESS_PER_MONITOR_DPI_AWARE = 2
        ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
        return
    except Exception:
        pass
    try:
        # Vista/7 : system-DPI aware (last resort)
        ctypes.windll.user32.SetProcessDPIAware()
    except Exception:
        pass


def setup_dpi_environment():
    """Set up DPI environment variables."""
    # Environment flags must be set before QApplication is created
    os.environ.setdefault("QT_ENABLE_HIGHDPI_SCALING", "1")
    os.environ.setdefault("QT_SCALE_FACTOR_ROUNDING_POLICY", "PassThrough")
    
    # Enable Windows DPI awareness
    _enable_win_per_monitor_dpi_awareness()
