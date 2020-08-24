# Mirai C2 Crasher
Mirai C2 Crasher exploits a certain part of the code to cause buffer overflow.
# Where is the vulnerability?
Right in [here](https://github.com/jgamblin/Mirai-Source-Code/blob/master/mirai/cnc/admin.go), on line number 225, it states: ```go buf := make([]byte, 1024)```, which means if the letters are bigger than "1024" it will cause buffer overflow, which basically will override the buffer and corrupt the data values that it was originally addressed to and crash the C2.
# Where did you find the vulnerability?
I wasn't the founder of the vulnerability, just wrote it in Python.
You can find the original vulnerability explained [here](https://securityaffairs.co/wordpress/85040/malware/mirai-servers-hack.html).
