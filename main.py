from kivy.lang import Builder

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

KV = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "#e7e4c0"
    text_color: "#4a4939"
    icon_color: "#4a4939"
    ripple_color: "#c5bdd2"
    selected_color: "#0c6c4d"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#4a4939"
    icon_color: "#4a4939"
    focus_behavior: False
    selected_color: "#4a4939"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:

            MDScreen:

                MDTopAppBar:
                    title: "Plants"
                    elevation: 4
                    pos_hint: {"top": 1}
                    md_bg_color: "#e7e4c0"
                    specific_text_color: "#4a4939"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
                Widget:
                    

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:            
                    title: "KivyMD library"
                    title_color: "#4a4939"
                    text: "Header text"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Mail"

                DrawerClickableItem:
                    icon: "gmail"
                    right_text: "+99"
                    text_right_color: "#4a4939"
                    text: "Inbox"

                DrawerClickableItem:
                    icon: "send"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Label"             
'''

class PlantsApp(MDApp):
    def build(self):
        # self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        # return Builder.load_string(
        #     '''MDScreen:
        #
        #         MDBottomNavigation:
        #             #panel_color: "#eeeaea"
        #             selected_color_background: "orange"
        #             text_color_active: "lightgrey"
        #
        #             MDBottomNavigationItem:
        #                 name: 'screen 1'
        #                 text: 'Mail'
        #                 icon: 'gmail'
        #                 badge_icon: "numeric-10"
        #
        #                 MDLabel:
        #                     text: 'Mail'
        #                     halign: 'center'
        #
        #             MDBottomNavigationItem:
        #                 name: 'screen 2'
        #                 text: 'Twitter'
        #                 icon: 'twitter'
        #                 badge_icon: "numeric-5"
        #
        #                 MDLabel:
        #                     text: 'Twitter'
        #                     halign: 'center'
        #
        #             MDBottomNavigationItem:
        #                 name: 'screen 3'
        #                 text: 'LinkedIN'
        #                 icon: 'linkedin'
        #
        #                 MDLabel:
        #                     text: 'LinkedIN'
        #                     halign: 'center'
        #     '''
        # )

        return Builder.load_string(KV)


PlantsApp().run()