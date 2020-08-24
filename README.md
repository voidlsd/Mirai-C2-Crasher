# Mirai C2 Crasher
Mirai C2 Crasher exploits a certain part of the code to cause buffer overflow.
# Where is the vulnerability?
[Here](https://github.com/jgamblin/Mirai-Source-Code/blob/master/mirai/cnc/admin.go) in the code, it states, "buf := make([]byte, 1024)", which if number bigger than "1024" will cause buffer overflow and crash the C2.
# Where did you find the vulnerability?
I wasn't the founder of the vulnerability, just wrote it in Python.
You can find the original vulnerability explained [here](https://securityaffairs.co/wordpress/85040/malware/mirai-servers-hack.html).
