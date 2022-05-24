import streamlit as st
import base64
from PIL import Image 


st.set_page_config(page_title="Personal Portfolio", layout="wide")

#---- USE LOCAL CSS----
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
		
local_css("style/style.css")
		
# ---- Show PDF ----
def show_pdf(file_path):
	with open(file_path, 'rb') as f:
		base64_pdf = base64.b64encode(f.read()).decode('utf-8')
	pdf_display = f'<iframe src="data:application/pdf;base64, {base64_pdf}" width="1175" height="900" type="application/pdf"></iframe>'
	st.markdown(pdf_display, unsafe_allow_html=True)
		
#show_pdf('docs/CV_for_Desire_Munyikwa.pdf')

#---- LOAD ASSETS ----
group_image = Image.open("images/grp_hwt.jpg")
my_image = Image.open("images/me1.jpg")
portal_image = Image.open("images/portal.jpg")
  
#---- HEADER SECTION ----
with st.container():
	image_col, right_col = st.columns((1,5))
	with image_col:
		st.image(my_image)
	with right_col:
		st.subheader("Hi, I am Desire Munyikwa :wave:")
	st.title("A GIS Developer/ Eng. Surveyor from Chisumbanje")
	st.write("I am passionate about GIS, RS and ways to automate daily tasks and develop decision support systems using python ")
	#st.write("[View CV](docs/CV_for_Desire_Munyikwa.pdf)")
	
	col1, col2, col3 = st.columns(3)
	with col1:
		if st.button('View CV', key='1'):
			show_pdf('docs/CV_for_Desire_Munyikwa.pdf')
			
	with col2:
		st.button('Close ', key='2')		
	with col3:
		with open('docs/CV_for_Desire_Munyikwa.pdf', 'rb') as pdf_file:
			PDFbyte = pdf_file.read()
		st.download_button(label = 'Dowload CV', key='3',
			data = PDFbyte,
			file_name = 'CV_for_Desire_Munyikwa.pdf',
			mime = 'application/octet-stream')
	
	
# ---- WHAT I DO ----
with st.container():
	st.write("---") #this displays a horizontal rule just like <hr> in html
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("What I do")
		st.write("##") #this inserts spacing below the header
		st.write("""
			- Map making/ cartography
			- WebGIS app development
			- Crop/ vegetation monitoring using RS
			- Data collection and cleaning
			- Engineering surveys (Topo, setting out, construction leveling) using GPS and AutoLevel
			- Spatial Data modelling
			- Website development
		""")
		
# ---- PROJECTS ----
with st.container():
	st.write("---")
	st.header("My Projects")
	st.write("##")
	image_column, text_column = st.columns((1,2)) #text column is twice as large as the image col
	with image_column:
		st.image(portal_image)
		with text_column:
			st.subheader("Greenfuel GIS portal")
			st.write("""
				I am currently developing a web application that displays interactive maps for all estates. The site includes an application to download maps and files.
				It has a third party [app](https://flurosense.com/app/maps/) to monitor crops using satellite data. Also, it includes a dashboard to show the major statistics and trend visualizations.
				[Visit Portal](http://172.16.5.94:8000)
			""")

# ---- CONTACT ----
with st.container():
	st.write("---")
	st.header("Get In Touch With Me")
	st.write("##")
	
	contact_form = """
	<form action="https://formsubmit.co/desiremunyikwa@gmail.com" method="POST">
		<input type="hidden" name="_captcha" value="false">
		<input type="text" name="name" placeholder="Your name" required>
		<input type="email" name="email" placeholder="Your email" required>
		<textarea name="message" placeholder="Write message" required></textarea>
		<button type="submit"> Send </button>
	</form>
	"""
	
	left_col, right_col = st.columns(2)
	with left_col:
		st.markdown(contact_form, unsafe_allow_html = True)
	with right_col:
		st.empty()
