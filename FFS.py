import fuzzing_1
import fuzzing_2
import fuzzing_3
import fuzzing_4
import fuzzing_5
import fuzzing_6
import fuzzing_7
import os
while True:
    print ("ZPAU Team ©")
    print ("1.English")
    print ("2.中文")
    choosein = input()
    choose = str(choosein)
    if len(choose) > 0:
        if choose == '1': #if celect Endlish
            #English UI
            print ("Please celect a module")
            print ("1.Test buffer capacity")
            print ("2.Send test package(AAA...)")
            print ("3.Generate random fuzz characters")
            print ("4.Send buff characters")
            print ("5.Calculate the exact position of the control instruction pointer")
            print ("6.Send fuzz characters to cover EIP")
            print ("7.Send bad character query character")
            print ("8.Test JMP ESP absolute address")
            print ("9.Send shellcode to run calculator")
            choose2in = input()
            choose2 = str(choose2in)
            if len(choose2) > 0:
                if choose2 == '1':
                    fuzzing_1.fuzzing1_e()
                elif choose2 == '2':
                    fuzzing_2.fuzzing2_e()
                elif choose2 == '3':
                    print ("Compile .\Project\FFS\scripts\pattern_create.rb with .\Project\FFS\bin\bin\ruby.exe")
                elif choose2 == '4':
                    fuzzing_3.fuzzing3_e()
                elif choose2 == '5':
                    print ("Compile .\Project\FFS\scripts\pattern_offset.rb with .\Project\FFS\bin\bin\ruby.exe")
                elif choose2 == '6':
                    fuzzing_4.fuzzing4_e()
                elif choose2 == '7':
                    fuzzing_5.fuzzing5_e()
                elif choose2 == '8':
                    fuzzing_6.fuzzing6_e()
                elif choose2 == '9':
                    fuzzing_7.fuzzing7_e()
                else:
                    print ("Error!")
            else:
                print("Error!")
        elif choose == '2':   #if celect Chinese
            #Chinese UI
            print ("请选择一个模块!")
            print ("1.测试缓冲区容量")
            print ("2.发送测试字符(AAA...)")
            print ("3.生成随机的模糊测试字符")
            print ("4.发送模糊测试字符")
            print ("5.计算控制指令指针的准确位置")
            print ("6.发送模糊测试字符以覆盖EIP")
            print ("7.发送坏字符测试的字符")
            print ("8.测试JMP ESP的绝对地址")
            print ("9.发送shellcode来运行计算器")
            choose2in = input()
            choose2 = str(choose2in)
            if len(choose2) > 0:
                if choose2 == '1':
                    fuzzing_1.fuzzing1_c()
                elif choose2 == '2':
                    fuzzing_2.fuzzing2_c()
                elif choose2 == '3':
                    os.system("编译 .\Project\FFS\scripts\pattern_create.rb 通过 .\Project\FFS\bin\bin\ruby.exe")
                elif choose2 == '4':
                    fuzzing_3.fuzzing3_c()
                elif choose2 == '5':
                    os.system("编译 .\Project\FFS\scripts\pattern_offset.rb 通过 .\Project\FFS\bin\bin\ruby.exe")
                elif choose2 == '6':
                    fuzzing_4.fuzzing4_c()
                elif choose2 == '7':
                    fuzzing_5.fuzzing5_c()
                elif choose2 == '8':
                    fuzzing_6.fuzzing6_c()
                elif choose2 == '9':
                    fuzzing_7.fuzzing7_c()
                else:
                    print ("错误!")
            else:
                print("Error!")
        else:
            print("Error!")
    else:
        print("Error!")