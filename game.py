from utils import show_notification, find_replace_bytes


class FreeFire(object):
    @staticmethod
    def apply_cheat(scan_hex, replace_hex, cheat_name):
        scan = bytes.fromhex(scan_hex)
        replace = bytes.fromhex(replace_hex)

        try:
            flag = find_replace_bytes(scan, replace)
            result = (
                f"{cheat_name} injectado" if flag else f"Fallo al injectar {cheat_name}"
            )
            show_notification(result)
        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def aimneck():
        FreeFire.apply_cheat(
            "62 6F 6E 65 5F 4E 65 63 6B", "62 6F 6E 65 5F 4E 65 63 73", "Aimneck"
        )

    @staticmethod
    def norecoil():
        FreeFire.apply_cheat(
            "00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED",
            "00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 00 00 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED",
            "No Recoil",
        )

    @staticmethod
    def onlyred():
        FreeFire.apply_cheat(
            "96 00 00 00 00 00 B0 40 00 00 80 3F 00 00 40 3F",
            "96 00 00 00 00 00 B8 40 00 00 00 00 00 00 00 00",
            "OnlyRed",
        )

    @staticmethod
    def clear_reports():
        FreeFire.apply_cheat(
            "0A 00 A0 E3 96 00 81 E0 00 00 51 E3 02 01 00 1A",
            "00 F0 20 E3",
            "Clear Reports",
        )

    @staticmethod
    def antiban():
        FreeFire.apply_cheat(
            "73 74 72 6F 6E 67 68 6F 6C 64",
            "73 74 72 6F 6E 67 64 69 73 61 62 6C 65",
            "Antiban",
        )

    @staticmethod
    def antiblacklist():
        FreeFire.apply_cheat(
            "47 61 6D 65 56 61 72 44 65 66",
            "43 68 65 61 74 69 6E 67 5F 4D 65 6D 6F 72 79 48 61 63 6B",
            "Anti blacklist",
        )

    @staticmethod
    def apply_antena(antena_name, scan_hex, replace_hex):
        FreeFire.apply_cheat(scan_hex, replace_hex, f"Antena {antena_name}")

    @staticmethod
    def female_hand():
        FreeFire.apply_antena(
            "Female Hand",
            "00 00 80 3F 31 F2 99 3E 60 55",
            "00 00 88 42 31 F2 99 3E 60 55",
        )

    @staticmethod
    def female_head():
        FreeFire.apply_antena(
            "Female Head", "00 00 80 3F FB 67 13 3F", "00 00 80 42 FB 67 13 3F"
        )

    @staticmethod
    def male_hand():
        FreeFire.apply_antena(
            "Male Hand", "00 00 80 3F 9F CD 7E BE", "00 00 88 42 9F CD 7E BE"
        )

    @staticmethod
    def male_head():
        FreeFire.apply_antena(
            "Male Head",
            "00 00 80 3F AC E5 22 BF C5 1F A0 BC",
            "00 00 80 42 AC E5 22 BF C5 1F A0 BC",
        )
