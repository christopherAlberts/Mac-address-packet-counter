# Mac-address-packet-counter
This code counts the amount of packets sent and received  with the same Mac address.

This code was designed to run on Linux.

## These are the two function contained in this code:

```
mac_des_count()     Counts the packets with the same destination Mac address.
```
*Output:*

```
     MAC DESTINATION COUNT
==============================
|       MAC       |  AMOUNT  |
==============================
Local MAC: A1:B2:C3:D4:E5:F6
------------------------------
01:00:5E:00:00:FB | 3
B8:EC:A3:2E:77:9A | 3
A1:B2:C3:D4:E5:F6 | 3
33:33:00:00:00:FB | 3
FF:FF:FF:FF:FF:FF | 3
------------------------------
```

```
mac_src_count()     Counts the packets with the same source Mac address.
```
*Output:*

```
       MAC SOURCE COUNT
==============================
|       MAC       |  AMOUNT  |
==============================
Local MAC: A1:B2:C3:D4:E5:F6
------------------------------
01:00:5E:00:00:FB | 3
B8:EC:A3:2E:77:9A | 3
A1:B2:C3:D4:E5:F6 | 3
33:33:00:00:00:FB | 3
FF:FF:FF:FF:FF:FF | 3
------------------------------
```

Just uncomment the function that you would like to run.
