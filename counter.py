from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

#Function to fix the window size
Window.size = (300,600)

calc = '''

BoxLayout:
	orientation:"vertical"
	
	ActionBar:
		
		ActionView:
		    padding:5
		    ActionPrevious:
		        title:"COUNTER APP"
		        with_previous:False
		        app_icon:''
		        	
		        Button:
		        	text:"Clear"
		        	on_release:
		        		app.func4(count,orange,green)
		
		
	MDLabel:
		id:orange
		text:""
		text_color:"white"
		bold:True
		halign:"center"
		font_style:"H6"
		theme_text_color: "Custom"
        md_bg_color: (255/255,127/255,0,1)
	
	MDLabel:
		id:count
		text:"0"
		halign:"center"
		font_style:"H1"
		text_color:"black"
		theme_text_color: "Custom"
        md_bg_color: (1,1,1,1)
		
	MDLabel:
		id:green
		text:""
		theme_text_color:"Custom"
		md_bg_color: (0,1,0,1)
		text_color:"white"
		bold:True
		halign:"center"
		font_style:"H6"
		
	BoxLayout:
		orientation:"horizontal"
		spacing:20
		padding:20

		MDRaisedButton:
			text:"+"
			bold:True
			size_hint:(.3,.7)
			background_color:(0,0,1,1)
			on_release:
				app.plus(count)
				app.func1(orange,count,green)
				
		MDRaisedButton:
			text:"_"
			bold:True
			size_hint:(.3,.7)
			background_color:(0,0,1,1)
			on_release:
				app.minus(count)
				app.func1(orange,count,green)
		

'''

class CounterApp(MDApp):
	def build(self):
		bldr = Builder.load_string(calc)
		return bldr
		
	def plus(self,count):
		a=int(count.text)
		a=a+1
		count.text= str(a)
		
	def minus(self,count):
		b=int(count.text)
		b=b-1
		count.text= str(b)
		
	def func1(self,orange,count,green):
		x=int(count.text)
		if (x>0):
			orange.text="+ POSITIVE +"
		elif (x<0):
			green.text="- NEGATIVE -"
		else:
			orange.text=""
			green.text=""
			
	def func4(self,count,orange,green):
			z= int(count.text)
			if(z!=0):
				count.text="0"
				green.text=""
				orange.text=""
			
		

CounterApp().run()