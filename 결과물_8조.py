mjan={}
mfeb={}
mmar={}
mapr={}
mmay={}
mjun={}
mjul={}
maug={}
msep={}
moct={}
mnov={}
mdec={}

sort_mjan={}
sort_mfeb={}
sort_mmar={}
sort_mapr={}
sort_mmay={}
sort_mjun={}
sort_mjul={}
sort_maug={}
sort_msep={}
sort_moct={}
sort_mnov={}
sort_mdec={}

while True:
                
    
    want=int(input("\n-----------------------------------------------\n원하는 번호를 선택해주세요.\n\n 1.내 일정 보기 \n\n 2.공휴일 보기(2022년) \n\n 3.일정 추가하기 \n\n 4.일정 삭제하기 \n\n :"))
    if want==1 :
        snum=int(input("\n몇 월의 일정을 보시겠습니까? "))
        if snum==1:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mjan)
            print("\n-------------------\n")
        elif snum==2:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mfeb)
            print("\n-------------------\n")
        elif snum==3:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mmar)
            print("\n-------------------\n")
        elif snum==4:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mapr)
            print("\n-------------------\n")
        elif snum==5:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mmay)
            print("\n-------------------\n")
        elif snum==6:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mjun)
            print("\n-------------------\n")
        elif snum==7:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mjul)
            print("\n-------------------\n")
        elif snum==8:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_maug)
            print("\n-------------------\n")
        elif snum==9:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_msep)
            print("\n-------------------\n")
        elif snum==10:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_moct)
            print("\n-------------------\n")
        elif snum==11:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mnov)
            print("\n-------------------\n")
        elif snum==12:
            print("\n-------------------\n",snum,"월 내 일정")
            print("\n",sort_mdec)
            print("\n-------------------\n")
        else:
            print("\n해당하는 달력이 없습니다.\n")

        end=input("프로그램을 종료하시겠습니까?\n예:y, 아니오: y를 제외한 아무 키를 입력하세요 : ")
        if end=="y": break
                

    

    elif want==2:

        i=int(input("\n원하는 달을 입력하세요: "))

        Jan = {'1일(토)' : '신정'}

        Feb = {'1일~3일(화~목)' : '설날'}

        Mar = {'1일(화)' : '3.1운동/삼일절'}

        Apr = {'없음' : 'X'}

        May = {'5일(목)' : '어린이날','8일(일)' : '부처님 오신 날'}

        Jun = {'6일(월)' : '현충일'}

        Jul = {'없음' : 'X'}

        Aug = {'15일(월)' : '광복절'}

        Sep = {'9일~11일(금~일)' : '추석'}

        Oct = {'3일(월)' : '개천절', '9일(일)' : '한글날'}

        Nov = {'없음' : 'X'}

        Dec = {'25일(일)' : '크리스마스'}


        

        if i==1: print("\n-------------------\n 2022년 1월 공휴일\n\n",Jan,"\n-------------------\n")
        elif i==2: print("\n-------------------\n 2022년 2월 공휴일\n\n",Feb,"\n-------------------\n")
        elif i==3: print("\n-------------------\n 2022년 3월 공휴일\n\n",Mar,"\n-------------------\n")
        elif i==4: print("\n-------------------\n 2022년 4월 공휴일\n\n",Apr,"\n-------------------\n")
        elif i==5: print("\n-------------------\n 2022년 5월 공휴일\n\n",May,"\n-------------------\n")
        elif i==6: print("\n-------------------\n 2022년 6월 공휴일\n\n",Jun,"\n-------------------\n")
        elif i==7: print("\n-------------------\n 2022년 7월 공휴일\n\n",Jul,"\n-------------------\n")
        elif i==8: print("\n-------------------\n 2022년 8월 공휴일\n\n",Aug,"\n-------------------\n")
        elif i==9: print("\n-------------------\n 2022년 9월 공휴일\n\n",Sep,"\n-------------------\n")
        elif i==10: print("\n-------------------\n 2022년10월 공휴일\n\n",Oct,"\n-------------------\n")
        elif i==11: print("\n-------------------\n 2022년 11월 공휴일\n\n",Nov,"\n-------------------\n")
        elif i==12: print("\n-------------------\n 2022년 12월 공휴일\n\n",Dec,"\n-------------------\n")
        else:print("\n해당하는 달력이 없습니다.\n")
        
        
        end=input("\n프로그램을 종료하시겠습니까?\n예:y, 아니오: y를 제외한 아무 키를 입력하세요 : ")
        if end=="y": break
                
    
        
    elif want==3:
        num=int(input("\n\n몇 월의 일정을 추가하시겠습니까?(예:1): "))

        if num==1:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                mjan[nntd]=ntd
                sort_mjan=sorted(mjan.items())
                print("\n-------------------\n 1월 일정\n\n",sort_mjan,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

            
        elif num==2:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<29:
                ntd=input("\n일정을 입력하세요: ")
                mfeb[nntd]=ntd
                sort_mfeb=sorted(mfeb.items())
                print("\n-------------------\n 2월 일정\n\n",sort_mfeb,"\n-------------------\n")
            else: print("\n",num,"월은 1~28일까지 있습니다.")

        elif num==3:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                mmar[nntd]=ntd
                sort_mmar=sorted(mmar.items())
                print("\n-------------------\n 3월 일정\n\n",sort_mmar,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

        elif num==4:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<31:
                ntd=input("\n일정을 입력하세요: ")
                mapr[nntd]=ntd
                sort_mapr=sorted(mapr.items())
                print("\n-------------------\n 4월 일정\n\n",sort_mapr,"\n-------------------\n")
            else: print("\n",num,"월은 1~30일까지 있습니다.")

        elif num==5:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                mmay[nntd]=ntd
                sort_mmay=sorted(mmay.items())
                print("\n-------------------\n 5월 일정\n\n",sort_mmay,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

        elif num==6:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<31:
                ntd=input("\n일정을 입력하세요: ")
                mjun[nntd]=ntd
                sort_mjun=sorted(mjun.items())
                print("\n-------------------\n 6월 일정\n\n",sort_mjun,"\n-------------------\n")
            else: print("\n",num,"월은 1~30일까지 있습니다.")

        elif num==7:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                mjul[nntd]=ntd
                sort_mjul=sorted(mjul.items())
                print("\n-------------------\n 7월 일정\n\n",sort_mjul,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")


        elif num==8:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                maug[nntd]=ntd
                sort_maug=sorted(maug.items())
                print("\n-------------------\n 8월 일정\n\n",sort_maug,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

        elif num==9:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<31:
                ntd=input("\n일정을 입력하세요: ")
                msep[nntd]=ntd
                sort_msep=sorted(msep.items())
                print("\n-------------------\n 9월 일정\n\n",sort_msep,"\n-------------------\n")
            else: print("\n",num,"월은 1~30일까지 있습니다.")

        elif num==10:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                moct[nntd]=ntd
                sort_moct=sorted(moct.items())
                print("\n-------------------\n 10월 일정\n\n",sort_moct,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

        elif num==11:
            nntd=int(input("날짜를 입력하세요(예:21): "))
            if 0<nntd<31:
                ntd=input("일정을 입력하세요: ")
                mnov[nntd]=ntd
                sort_mnov=sorted(mnov.items())
                print("\n-------------------\n 11월 일정\n\n",sort_mnov,"\n-------------------\n")
            else: print("\n",num,"월은 1~30일까지 있습니다.")

        elif num==12:
            nntd=int(input("\n날짜를 입력하세요(예:21): "))
            if 0<nntd<32:
                ntd=input("\n일정을 입력하세요: ")
                mdec[nntd]=ntd
                sort_mdec=sorted(mdec.items())
                print("\n-------------------\n 12월 일정\n\n",sort_mdec,"\n-------------------\n")
            else: print("\n",num,"월은 1~31일까지 있습니다.")

        else:
            print("\n해당하는 달력이 없습니다.\n")

        end=input("\n프로그램을 종료하시겠습니까?\n예:y, 아니오: y를 제외한 아무 키를 입력하세요 : ")
        if end=="y": break
                
 
    

    elif want==4:
        dmon=int(input("\n\n몇 월의 일정을 삭제하시겠습니까? "))
        
        if dmon==1:
            print("\n1월 전체 일정\n\n",sort_mjan,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))

            if delt!=0 and 0<delt<32:
                del mjan[delt]
                sort_mjan=sorted(mjan.items())
                print("------------------------------\n1월 남은 일정\n\n",sort_mjan)
                
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            
            

            
        elif dmon==2:
            print("\n2월 전체 일정\n\n",sort_mfeb,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))

            if delt!=0 and 0<delt<29:
                del mfeb[delt]
                sort_mfeb=sorted(mfeb.items())
                print("------------------------------\n2월 남은 일정\n",sort_mfeb)
                
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")

            

        elif dmon==3:
            print("\n3월 전체 일정\n\n",sort_mmar,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))

            if delt!=0 and 0<delt<32:
                del mmar[delt]
                sort_mmar=sorted(mmar.items())
                print("------------------------------\n3월 남은 일정\n",sort_mmar)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            

        elif dmon==4:
            print("------------------------------\n4월 전체 일정\n",sort_mapr,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<31:
                del mapr[delt]
                sort_mapr=sorted(mapr.items())
                print("------------------------------\n4월 남은 일정\n",sort_mapr)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            

        elif dmon==5:
            print("------------------------------\n5월 전체 일정\n",sort_mmay,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<32:
                del mmay[delt]
                sort_mmay=sorted(mmay.items())
                print("------------------------------\n5월 남은 일정\n",sort_mmay)

            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")            

        elif dmon==6:
            print("------------------------------\n6월 전체 일정\n",sort_mjun,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<31:
                del mjun[delt]
                sort_mjun=sorted(mjun.items())
                print("------------------------------\n6월 남은 일정\n",sort_mjun)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            
        
        elif dmon==7:
            print("------------------------------\n7월 전체 일정\n",sort_mjul,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<32:
                del mjul[delt]
                sort_mjul=sorted(mjul.items())
                print("------------------------------\n7월 남은 일정\n",sort_mjul)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            
        
        elif dmon==8:
            print("------------------------------\n8월 전체 일정\n",sort_maug,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<32:
                del maug[delt]
                sort_maug=sorted(maug.items())
                print("------------------------------\n8월 남은 일정\n",sort_maug)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            
        
        elif dmon==9:
            print("------------------------------\n9월 전체 일정\n",sort_msep,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<31:
                del msep[delt]
                sort_msep=sorted(msep.items())
                print("------------------------------\n9월 남은 일정\n",sort_msep)

            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")

            
        elif dmon==10:
            print("------------------------------\n10월 전체 일정\n",sort_moct,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<32:
                del moct[delt]
                sort_moct=sorted(moct.items())
                print("------------------------------\n10월 남은 일정\n",sort_moct)


        elif dmon==11:
            print("------------------------------\n11월 전체 일정\n",sort_mnov,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<31:
                del mnov[delt]
                sort_mnov=sorted(mnov.items())
                print("------------------------------\n11월 남은 일정\n",sort_mnov)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")
            
    
        elif dmon==12:
            print("------------------------------\n12월 전체 일정\n",sort_mdec,"\n")
            delt=int(input("며칠의 일정을 삭제하시겠습니까?(일정이 없을 경우 0입력) :"))
            if delt!=0 and 0<delt<32:
                del mdec[delt]
                sort_mdec=sorted(mdec.items())
                print("------------------------------\n12월 남은 일정\n",sort_mdec)
            elif delt==0: print("취소할 일정이 없습니다\n")
            
            else: print("\n정보가 잘못 입력되었습니다.")

            
        else:
            print("\n해당하는 달력이 없습니다.\n")
            

        end=input("프로그램을 종료하시겠습니까?\n예:y, 아니오: y를 제외한 아무 키를 입력하세요 : ")
        if end=="y": break

    else:
        print("번호를 다시 입력해주세요.")
