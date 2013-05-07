00000000  7F45              jg 0x47
00000002  4C                dec sp
00000003  46                inc si
00000004  0101              add [bx+di],ax
00000006  0100              add [bx+si],ax
00000008  0000              add [bx+si],al
0000000A  0000              add [bx+si],al
0000000C  0000              add [bx+si],al
0000000E  0000              add [bx+si],al
00000010  0200              add al,[bx+si]
00000012  0300              add ax,[bx+si]
00000014  0100              add [bx+si],ax
00000016  0000              add [bx+si],al
00000018  B88004            mov ax,0x480
0000001B  0834              or [si],dh
0000001D  0000              add [bx+si],al
0000001F  00880100          add [bx+si+0x1],cl
00000023  0000              add [bx+si],al
00000025  0000              add [bx+si],al
00000027  0034              add [si],dh
00000029  0020              add [bx+si],ah
0000002B  0003              add [bp+di],al
0000002D  0028              add [bx+si],ch
0000002F  0003              add [bp+di],al
00000031  0002              add [bp+si],al
00000033  0001              add [bx+di],al
00000035  0000              add [bx+si],al
00000037  0000              add [bx+si],al
00000039  0000              add [bx+si],al
0000003B  0000              add [bx+si],al
0000003D  800408            add byte [si],0x8
00000040  00800408          add [bx+si+0x804],al
00000044  7401              jz 0x47 ; If modified to jnz, +++ killed by SIGKILL +++
00000046  0000              add [bx+si],al
00000048  7401              jz 0x4b
0000004A  0000              add [bx+si],al
0000004C  050000            add ax,0x0
0000004F  0000              add [bx+si],al
00000051  1000              adc [bx+si],al
00000053  0004              add [si],al
00000055  0000              add [bx+si],al
00000057  0000              add [bx+si],al
00000059  0000              add [bx+si],al
0000005B  0000              add [bx+si],al
0000005D  0000              add [bx+si],al
0000005F  0000              add [bx+si],al
00000061  0000              add [bx+si],al
00000063  0000              add [bx+si],al
00000065  0000              add [bx+si],al
00000067  0000              add [bx+si],al
00000069  0000              add [bx+si],al
0000006B  0004              add [si],al
0000006D  0000              add [bx+si],al
0000006F  0004              add [si],al
00000071  0000              add [bx+si],al
00000073  0051E5            add [bx+di-0x1b],dl
00000076  7464              jz 0xdc
00000078  0000              add [bx+si],al
0000007A  0000              add [bx+si],al
0000007C  0000              add [bx+si],al
0000007E  0000              add [bx+si],al
00000080  0000              add [bx+si],al
00000082  0000              add [bx+si],al
00000084  0000              add [bx+si],al
00000086  0000              add [bx+si],al
00000088  0000              add [bx+si],al
0000008A  0000              add [bx+si],al
0000008C  06                push es
0000008D  0000              add [bx+si],al
0000008F  0004              add [si],al
00000091  0000              add [bx+si],al
00000093  0000              add [bx+si],al
00000095  0000              add [bx+si],al
00000097  0000              add [bx+si],al
00000099  0000              add [bx+si],al
0000009B  0000              add [bx+si],al
0000009D  0000              add [bx+si],al
0000009F  0000              add [bx+si],al
000000A1  0000              add [bx+si],al
000000A3  0000              add [bx+si],al
000000A5  0000              add [bx+si],al
000000A7  0000              add [bx+si],al
000000A9  0000              add [bx+si],al
000000AB  0000              add [bx+si],al
000000AD  0000              add [bx+si],al
000000AF  0000              add [bx+si],al
000000B1  0000              add [bx+si],al
000000B3  0000              add [bx+si],al
000000B5  0000              add [bx+si],al
000000B7  005589            add [di-0x77],dl
000000BA  E557              in ax,0x57
000000BC  56                push si
000000BD  53                push bx
000000BE  83EC10            sub sp,byte +0x10
000000C1  8B4504            mov ax,[di+0x4]
000000C4  8D7D08            lea di,[di+0x8]
000000C7  8945F0            mov [di-0x10],ax
000000CA  31D2              xor dx,dx
000000CC  B81A00            mov ax,0x1a
000000CF  0000              add [bx+si],al
000000D1  89D3              mov bx,dx
000000D3  89D1              mov cx,dx
000000D5  89D6              mov si,dx
000000D7  CD80              int 0x80 ; System interruption system_call, Replace this by two nops, change by 9090
000000D9  85C0              test ax,ax
000000DB  755F              jnz 0x13c ; Debug Proection jump
000000DD  837DF002          cmp word [di-0x10],byte +0x2
000000E1  7559              jnz 0x13c ; Debug protection jump
000000E3  8B7F04            mov di,[bx+0x4]
000000E6  897DE4            mov [di-0x1c],di
000000E9  C745E83905        mov word [di-0x18],0x539
000000EE  0000              add [bx+si],al
000000F0  EB39              jmp short 0x12b
000000F2  6945E8A741        imul ax,[di-0x18],word 0x41a7
000000F7  0000              add [bx+si],al
000000F9  8945F0            mov [di-0x10],ax
000000FC  BEFFFF            mov si,0xffff
000000FF  FF07              inc word [bx]
00000101  31D2              xor dx,dx
00000103  F7F6              div si
00000105  8955E8            mov [di-0x18],dx
00000108  89FE              mov si,di
0000010A  2B75E4            sub si,[di-0x1c]
0000010D  83FE2B            cmp si,byte +0x2b
00000110  7715              ja 0x127
00000112  81E2FF00          and dx,0xff
00000116  0000              add [bx+si],al
00000118  31D1              xor cx,dx
0000011A  0FB6864881        movzx ax,[bp-0x7eb8]
0000011F  0408              add al,0x8
00000121  39C1              cmp cx,ax
00000123  7502              jnz 0x127
00000125  EB03              jmp short 0x12a
00000127  83CBFF            or bx,byte -0x1
0000012A  47                inc di
0000012B  0FBE0F            movsx cx,[bx]
0000012E  84C9              test cl,cl
00000130  75C0              jnz 0xf2
00000132  2B7DE4            sub di,[di-0x1c]
00000135  83FF2B            cmp di,byte +0x2b
00000138  7602              jna 0x13c
0000013A  EB03              jmp short 0x13f
0000013C  83CBFF            or bx,byte -0x1
0000013F  B80100            mov ax,0x1
00000142  0000              add [bx+si],al
00000144  CD80              int 0x80 ; System interruption system_call -- Removing this line, the program is stopped
00000146  EBFE              jmp short 0x146 ; Infinite loop....
00000148  61                popaw
00000149  A96E07            test ax,0x76e
0000014C  F1                int1
0000014D  BA8B95            mov dx,0x958b
00000150  44                inc sp
00000151  93                xchg ax,bx
00000152  50                push ax
00000153  21F2              and dx,si
00000155  8F01              pop word [bx+di]
00000157  A154F8            mov ax,[0xf854]
0000015A  638C5E59          arpl [si+0x595e],cx
0000015E  89794D            mov [bx+di+0x4d],di
00000161  B20E              mov dl,0xe
00000163  6BA4C5136B        imul sp,[si+0x13c5],byte +0x6b
00000168  78F4              js 0x15e
0000016A  43                inc bx
0000016B  7A03              jpe 0x170
0000016D  9B756C            wait jnz 0x1dc
00000170  8BFD              mov di,bp
00000172  96                xchg ax,si
00000173  81002E73          add word [bx+si],0x732e
00000177  687374            push word 0x7473
0000017A  7274              jc 0x1f0
0000017C  61                popaw
0000017D  6200              bound ax,[bx+si]
0000017F  2E7465            cs jz 0x1e7
00000182  7874              js 0x1f8
00000184  0000              add [bx+si],al
00000186  0000              add [bx+si],al
00000188  0000              add [bx+si],al
0000018A  0000              add [bx+si],al
0000018C  0000              add [bx+si],al
0000018E  0000              add [bx+si],al
00000190  0000              add [bx+si],al
00000192  0000              add [bx+si],al
00000194  0000              add [bx+si],al
00000196  0000              add [bx+si],al
00000198  0000              add [bx+si],al
0000019A  0000              add [bx+si],al
0000019C  0000              add [bx+si],al
0000019E  0000              add [bx+si],al
000001A0  0000              add [bx+si],al
000001A2  0000              add [bx+si],al
000001A4  0000              add [bx+si],al
000001A6  0000              add [bx+si],al
000001A8  0000              add [bx+si],al
000001AA  0000              add [bx+si],al
000001AC  0000              add [bx+si],al
000001AE  0000              add [bx+si],al
000001B0  0B00              or ax,[bx+si]
000001B2  0000              add [bx+si],al
000001B4  0100              add [bx+si],ax
000001B6  0000              add [bx+si],al
000001B8  06                push es
000001B9  0000              add [bx+si],al
000001BB  00B88004          add [bx+si+0x480],bh
000001BF  08B80000          or [bx+si+0x0],bh
000001C3  00BC0000          add [si+0x0],bh
000001C7  0000              add [bx+si],al
000001C9  0000              add [bx+si],al
000001CB  0000              add [bx+si],al
000001CD  0000              add [bx+si],al
000001CF  0004              add [si],al
000001D1  0000              add [bx+si],al
000001D3  0000              add [bx+si],al
000001D5  0000              add [bx+si],al
000001D7  0001              add [bx+di],al
000001D9  0000              add [bx+si],al
000001DB  0003              add [bp+di],al
000001DD  0000              add [bx+si],al
000001DF  0000              add [bx+si],al
000001E1  0000              add [bx+si],al
000001E3  0000              add [bx+si],al
000001E5  0000              add [bx+si],al
000001E7  007401            add [si+0x1],dh
000001EA  0000              add [bx+si],al
000001EC  1100              adc [bx+si],ax
000001EE  0000              add [bx+si],al
000001F0  0000              add [bx+si],al
000001F2  0000              add [bx+si],al
000001F4  0000              add [bx+si],al
000001F6  0000              add [bx+si],al
000001F8  0100              add [bx+si],ax
000001FA  0000              add [bx+si],al
000001FC  0000              add [bx+si],al
000001FE  0000              add [bx+si],al
