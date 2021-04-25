## create device banners

### description:
Just give this function a hostname and model type and it will
creates standard exec and login banners for a cisco device.

you can vary the segment sizes, by adjusting list(segments). The total
segment space can't be larger than 61 characters.

> **param hostname:** (str) The device hostname<br>
> **param model:** (str) The device model<br>
> **returns:** (str) the config text containing the two banners.<br>


```text
banner exec ~
  +-----------+------------------------------------+--------------+
  |  AT&T-C4  |          NA-CA-SFC-PE-01           |   ASR-9910   |
  +-----------+------------------------------------+--------------+
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

```
