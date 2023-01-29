from dbhelper import DBhelper
def main():
    d=DBhelper()
    while True:
        print("press 1 for insert")
        print("press 2 for delete")
        print("press 3 for update")
        print("press 4 for display")
        print("press 5 for exit")
        try:
            t=int(input("choice: "))
            if t==1:
                print("insert")
                n=int(input("give user id: "))
                m=input("give name: ")
                k=input("phone: ")
                d.insert_user(n,m,k)
            elif t==2:
                print("delete")
                n = int(input("give user id: "))
                d.delete(n)
            elif t==3:
                print("update")
                n = int(input("give user id: "))
                m = input("give name: ")
                k = input("phone: ")
                d.update(n,m,k)
            elif t==4:
                print("display")
                d.fetch_all()
            elif t==5:
                break
            else:
                print("invalid")
        except Exception as e:
            print(e)
            print("invalid")


if __name__=="__main__":
    main()




