import ctypes
from ctypes import wintypes
import pymem
from windows_toasts import WindowsToaster, ToastText1
from settings import APP_NAME, PROCESS_NAME


def find_replace_bytes(pattern: bytes, replacement: bytes) -> bool:
    process = pymem.Pymem(PROCESS_NAME)
    show_notification('Buscando secuencia de bytes')

    address = pymem.pattern.pattern_scan_all(process.process_handle, pattern)

    if address:
        address_ptr = ctypes.c_void_p(address)

        old_protect = wintypes.DWORD()
        PAGE_EXECUTE_READWRITE = 0x40
        ctypes.windll.kernel32.VirtualProtectEx(process.process_handle, address_ptr, len(replacement),
                                                PAGE_EXECUTE_READWRITE, ctypes.byref(old_protect))
        process.write_bytes(address, replacement, len(replacement))
        ctypes.windll.kernel32.VirtualProtectEx(process.process_handle, address_ptr, len(replacement), old_protect,
                                                ctypes.byref(old_protect))
        return True
    else:
        return False


def show_notification(message: str) -> None:
    wintoaster = WindowsToaster(APP_NAME)
    toast = ToastText1()
    toast.SetBody(message)
    wintoaster.show_toast(toast)

