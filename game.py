from utils import show_notification, find_replace_bytes


class FreeFire(object):
    @staticmethod
    def aimneck():
        aim_scan = bytes.fromhex("62 6F 6E 65 5F 4E 65 63 6B")
        aim_replace = bytes.fromhex("62 6F 6E 65 5F 4E 65 63 73")

        neck_scan = bytes.fromhex(
            "53 68 61 64 6F 77 49 6E 74 65 6E 73 69 79 62 6F 6E 65 5F 48 69 70 73"
        )
        neck_replace = bytes.fromhex(
            "53 68 61 64 6F 77 49 6E 74 65 6E 73 69 79 62 6F 6E 65 5F 4E 65 63 6B"
        )

        try:
            find_replace_bytes(aim_scan, aim_replace)
            flag = find_replace_bytes(neck_scan, neck_replace)
            show_notification("Aimneck injectado" if flag else "Fallo al injectar")

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def norecoil():
        scan = bytes.fromhex(
            "00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 7A 44 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED"
        )
        replace = bytes.fromhex(
            "00 0A 81 EE 10 0A 10 EE 10 8C BD E8 00 00 00 00 F0 48 2D E9 10 B0 8D E2 02 8B 2D ED"
        )

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification("No Recoil injectado" if flag else "Fallo al injectar")

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def onlyred():
        scan = bytes.fromhex("96 00 00 00 00 00 B0 40 00 00 80 3F 00 00 40 3F")
        replace = bytes.fromhex("96 00 00 00 00 00 B8 40 00 00 00 00 00 00 00 00")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification("OnlyRed injectado" if flag else "Fallo al injectar")

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def clear_reports():
        scan = bytes.fromhex("0A 00 A0 E3 96 00 81 E0 00 00 51 E3 02 01 00 1A")
        replace = bytes.fromhex("00 F0 20 E3")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Clear Reports injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def antiban():
        scan = bytes.fromhex("73 74 72 6F 6E 67 68 6F 6C 64")
        replace = bytes.fromhex("73 74 72 6F 6E 67 64 69 73 61 62 6C 65")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification("Antiban injectado" if flag else "Fallo al injectar")

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def antiblacklist():
        scan = bytes.fromhex("47 61 6D 65 56 61 72 44 65 66")
        replace = bytes.fromhex(
            "43 68 65 61 74 69 6E 67 5F 4D 65 6D 6F 72 79 48 61 63 6B"
        )

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Anti blacklist injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def female_hand():
        scan = bytes.fromhex("00 00 80 3F 31 F2 99 3E 60 55")
        replace = bytes.fromhex("00 00 88 42 31 F2 99 3E 60 55")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Antena Female Hand injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def female_head():
        scan = bytes.fromhex("00 00 80 3F FB 67 13 3F")
        replace = bytes.fromhex("00 00 80 42 FB 67 13 3F")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Antena Female Head injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def male_hand():
        scan = bytes.fromhex("00 00 80 3F 9F CD 7E BE")
        replace = bytes.fromhex("00 00 88 42 9F CD 7E BE")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Antena Male Hand injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def male_head():
        scan = bytes.fromhex("00 00 80 3F AC E5 22 BF C5 1F A0 BC")
        replace = bytes.fromhex("00 00 80 42 AC E5 22 BF C5 1F A0 BC")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Antena Male Head injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))

    @staticmethod
    def antena():
        scan = bytes.fromhex("00 00 80 3F CF F7 AD 34")
        replace = bytes.fromhex("33 33 34 43 CF F7 AD 34")

        try:
            flag = find_replace_bytes(scan, replace)
            show_notification(
                "Antena Male Head injectado" if flag else "Fallo al injectar"
            )

        except Exception as e:
            show_notification(str(e))
