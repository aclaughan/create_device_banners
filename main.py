import logging

logging.basicConfig(level=logging.INFO, filename="app.log")


def create_device_banners(hostname: str, model: str) -> str:
    """
    Just give this function a hostname and model type and it will
    creates standard exec and login banners for a cisco device.

    you can vary the segment sizes, by adjusting list(segments). The total
    segment space can't be larger than 61 characters.

    :param hostname: (str) The device hostname
    :param model: (str) The device model
    :return: (str) the config text containing the two banners.
    """
    logging.info(f"hostname: {hostname}, model: {model}")
    segments = [11, 36, 14]
    info = ['AT&T-C4', hostname, model]

    frame = "  +"
    e_ban = "  |"

    for index, segment in enumerate(segments):
        frame += f"{'-' * segment}+"
        e_ban += f"{info[index]:^{segment}}|"

    logging.info(e_ban)

    return f"""
banner exec ~
{frame}
{e_ban.upper()}
{frame}
~
!
banner login ~
  +---------------------------------------------------------------+
  |                                                               |
  |                         LEGAL NOTICE                          |
  |                                                               |
  |       UNAUTHORISED ACCESS TO THIS DEVICE IS PROHIBITED        |
  |                                                               |
  | You must have explicit, authorised permission to access or    |
  | configure this device. Unauthorised attempts and actions to   |
  | access or use this system may result in civil and/or criminal |
  | penalties. All activities performed on this device are logged |
  | and monitored.                                                |
  |                                                               |
  +---------------------------------------------------------------+
~
!
"""


def main():
    print(create_device_banners(hostname="na-ca-sfc-pe-01", model="asr-9910"))


if __name__ == "__main__":
    main()
