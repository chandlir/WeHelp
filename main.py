import data
import ui


def main():
    data.init()
    while True:
        act1 = ui.prompt_for_action1()
        if act1 == 'QUIT':
            break
        elif act1 == 'LOG_IN':
            res1 = ui.LOG_IN()
            if res1 == 'QUIT':
                break
            elif res1 == 'SIGN IN':
                res2 = ui.SIGN_IN()
                userinfo = res2
            else:
                userinfo = res1
        else:
            res1 = ui.SIGN_IN()
            userinfo = res1
        uid = userinfo[0]

        while True:
            act2 = ui.prompt_for_action2()
            if act2 == 'LOG_OUT':
                break
            elif act2 == 'ADD_ITEMS':
                ui.ADD_ITEMS(uid)
            elif act2 == 'DELETE_ITEMS':
                ui.DELETE_ITEMS(uid)
            elif act2 == 'VIEW_MY_ITEMS':
                ui.VIEW_MY_ITEMS(uid)
            elif act2 == 'VIEW_ALL_ITEMS':
                ui.VIEW_ALL_ITEMS()
            elif act2 == 'SEARCH_ITEMS':
                ui.SEARCH_ITEMS()


if __name__ == "__main__": main()













