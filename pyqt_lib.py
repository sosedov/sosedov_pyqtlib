
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon
from functools import partial
#from technotrader import tables_list

def alert(main_window,text_header,alert_text):
	from PyQt5.QtWidgets import QMessageBox
	button_reply=QMessageBox.question(main_window,text_header,alert_text,QMessageBox.Yes,QMessageBox.Yes)
	return 1

def confirm(main_window,text_header,alert_text):
	from PyQt5.QtWidgets import QMessageBox
	button_reply=QMessageBox.question(main_window,text_header,alert_text,QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
	if button_reply==QMessageBox.Yes:
		return 1
	else:
		return 0

def make_scroll(w,app_width,app_height):
	from PyQt5.QtCore import Qt
	from PyQt5.QtWidgets import QScrollArea,QScroller
	scroll_area = QScrollArea(w)
	scroll_area.setGeometry(0,0,app_width,app_height)
	#scroll_area.setWidget(scroll_widget)
	QScroller.grabGesture(scroll_area.viewport(), QScroller.LeftMouseButtonGesture)
	scroll_area.setWidgetResizable(True)
	#scroll.setWidgetResizable(True)
	#scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
	#scroll.resize(app_width,app_height)
	return scroll_area

def create_layer(app_width,app_height,app_left,app_right,title,icon_path,mw):
	from PyQt5.QtWidgets import QWidget
	if mw==0:
		w=QWidget()
	else:
		w=QWidget(mw)
	w.resize(app_width,app_height)
	w.move(app_left,app_right)
	w.setWindowTitle(title)
	if icon_path!='':
		from PyQt5.QtGui import QIcon
		w.setWindowIcon(QIcon(icon_path))
	return w

def add_pb(w,left,top,color):
	from PyQt5.QtCore import QRect, QPropertyAnimation
	pb=QPushButton("",w)
	pb.move(left,top)
	pb.resize(26,26)
	pb.setStyleSheet("border-radius:13px;background-color:"+str(color)+";")
	return pb

def add_background(w,wi,he,left,top,isimg,backval):
	from PyQt5.QtWidgets import QFrame
	background_img=QFrame(w)
	background_img.resize(wi,he)
	background_img.move(left,top)
	if isimg==1:
		background_img.setStyleSheet("border-image:url("+str(backval)+") 0 0 0 0 stretch;")
	else:
		background_img.setStyleSheet("background-color:"+str(backval)+";")
	return background_img

def add_text(text,w,left,top,font_family,font_size,text_align,bold=0,color="black"):
	from PyQt5.QtWidgets import QLabel
	from PyQt5.QtGui import QFont
	new_text=QLabel(w)
	new_text.setText(text)
	alignment_val=""
	if text_align=="center":
		alignment_val="text-align:center;"
	elif text_align=="right":
		alignment_val="text-align:right;"
	new_text.setFont(QFont('SansSerif', font_size))
	if font_family!='SansSerif' or font_family!='':
		new_text.setFont(QFont(font_family, font_size))
	new_text.setStyleSheet('color:'+str(color)+';'+str(alignment_val))
	#if bold!=0:
	#	new_text.setBold(True)
	new_text.move(left,top)
	return new_text

def setid(obj,newid,istable=0):
	if istable==0:
		obj.setObjectName(str(newid))
	else:
		from technotrader import tables_list
		tables_list[newid]=obj

def get_el_by_id(main_window,hide_layer_id,istable=0):
	from PyQt5.QtCore import QObject
	try:
		if istable==0:
			thisrl=main_window.findChild(QObject,str(hide_layer_id))
			return thisrl
		else:
			from technotrader import tables_list
			thisel=tables_list[hide_layer_id]
			return thisel
	except Exception:
		return 0



def add_button(w,button_text,wi,he,left,top,tooltip,classname,btn_icon="none"):
	from PyQt5.QtWidgets import QPushButton
	from PyQt5.QtGui import QPixmap,QIcon
	if w==0:
		btn=QPushButton(button_text)
	else:
		btn=QPushButton(button_text,w)
	if tooltip!="":
		btn.setToolTip(tooltip)
	if wi==0 and he==0:
		btn.resize(btn.sizeHint())
	else:
		btn.resize(wi,he)
	btn.move(left,top)
	if classname!='':
		btn.setProperty("styleclass",classname)
	if btn_icon!="none":
		icon  = QPixmap(btn_icon)
		btn.setIcon(QIcon(icon))
	return btn

def add_input(w,label_text,wi,he,left,top,type,label_color="black"):
	from PyQt5.QtGui import QFont,QDoubleValidator
	from PyQt5.QtWidgets import QLineEdit,QLabel
	lbl=QLabel(w)
	lbl.setText(label_text)
	lbl.setFont(QFont("Arial",10))
	lbl.move(left+10,top)
	lbl.setStyleSheet("color:"+str(label_color)+";")
	e1 = QLineEdit(w)
	e1.setFont(QFont("Arial",15))
	e1.resize(wi,he)
	e1.move(left,top+18)
	e1.setStyleSheet("border:1px solid black;")
	if type=="password":
		e1.setEchoMode(QLineEdit.Password)
	elif type=="number":
		e1.setValidator(QDoubleValidator(999999, -999999, 8))
	return [e1,lbl]

def add_checkbox(w,label_text,fontsize,left,top,label_color="black"):
	from PyQt5.QtGui import QFont
	from PyQt5.QtWidgets import QCheckBox
	chk=QCheckBox(label_text,w)
	chk.move(left,top)
	chk.setFont(QFont("Arial",fontsize))
	chk.setStyleSheet("color:"+str(label_color)+";")
	return chk

def add_select(w,label_text,arr_select,wi,he,left,top,label_color="black"):
	from PyQt5.QtGui import QFont
	from PyQt5.QtWidgets import QComboBox,QLabel
	lbl=QLabel(w)
	lbl.setText(label_text)
	lbl.setFont(QFont("Arial",10))
	lbl.move(left+10,top)
	lbl.setStyleSheet("color:"+str(label_color)+";")
	select=QComboBox(w)
	select.setFont(QFont("Arial",15))
	select.resize(wi,he)
	select.move(left,top+18)
	select.setStyleSheet("border:2px solid black;")
	for option in arr_select:
		select.addItem(option)
	return [select,lbl]

def go2menu(main_window,layer_hide):
	hide_layer=get_el_by_id(main_window,layer_hide)
	show_layer=get_el_by_id(main_window,"menu_layer")
	hide_layer.hide()
	show_layer.show()


def setHeader(w,text,wi,main_window,layer=""):
	add_background(w,wi,50,0,0,0,"rgb(10,15,63)")
	btn=add_button(w,"Назад",150,50,0,0,"","btn_dark")
	btn.clicked.connect(partial(go2menu,main_window,layer))
	add_text(text,w,wi/2,10,"SansSerif",15,"",1,"white")

def add_table(w,left,top,wi,header_arr,content_arr,readonly=True):
	from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem,QAbstractScrollArea,QHeaderView
	from PyQt5.QtCore import Qt
	if not w==0:
		table = QTableWidget(w)
	else:
		table = QTableWidget()
	table.move(left,top)
	table.setMinimumWidth(int(wi))
	table.setMaximumWidth(int(wi)+1)
	table.setColumnCount(len(header_arr))     # Устанавливаем три колонки
	table.setRowCount(len(content_arr))        # и одну строку в таблице
	table.setHorizontalHeaderLabels(header_arr)
	j=0
	for row in content_arr:
		jj=0
		for field in row:
			if readonly==True:
				this_item=QTableWidgetItem(field)
				this_item.setFlags(Qt.ItemIsEnabled)
				table.setItem(j, jj, this_item)
			else:
				table.setItem(j, jj, QTableWidgetItem(field))
			jj+=1
		j+=1
	table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
	header = table.horizontalHeader()
	z=0
	while(z<len(header_arr)):
		header.setSectionResizeMode(z, QHeaderView.Stretch)
		z+=1
	table.resizeColumnsToContents()
	table.resizeRowsToContents()
	return table

def add_scroll_table(w,left,top,wi,he,header_arr,content_arr):
	from PyQt5.QtWidgets import  QTableWidgetItem,QScrollArea,QWidget,QGridLayout,QFormLayout,QScroller
	scroll_area = QScrollArea(w)
	scroll_area.setGeometry(left,top,wi,he)
	layout = QGridLayout()
	layout.addWidget(scroll_area)
	scroll_widget = QWidget()
	scroll_layout = QFormLayout(scroll_widget)
	this_tab=add_table(0,left,top,wi-20,header_arr,content_arr)
	scroll_layout.addRow(this_tab)
	scroll_area.setWidget(scroll_widget)
	QScroller.grabGesture(scroll_area.viewport(), QScroller.LeftMouseButtonGesture)
	scroll_area.setWidgetResizable(True)
	return [scroll_area,this_tab]

def add_textarea(w,label_text,wi,he,left,top,type,label_color="black"):
	from PyQt5.QtGui import QFont,QDoubleValidator
	from PyQt5.QtWidgets import QPlainTextEdit,QLabel
	lbl=QLabel(w)
	lbl.setText(label_text)
	lbl.setFont(QFont("Arial",10))
	lbl.move(left+10,top)
	lbl.setStyleSheet("color:"+str(label_color)+";")
	e1 = QPlainTextEdit(w)
	e1.setFont(QFont("Arial",15))
	e1.resize(wi,he)
	e1.move(left,top+18)
	e1.setStyleSheet("border:2px solid black;")
	return [e1,lbl]

def show_pb(main_window,this_layer):
	get_el_by_id(main_window,this_layer).hide()
	get_el_by_id(main_window,"pb_layer").show()
	get_el_by_id(main_window,"pb_layer_alert_layer_pb_text").setVisible(True)
	get_el_by_id(main_window,"pb_layer_alert_layer_textarea").setVisible(False)
	get_el_by_id(main_window,"pb_layer_alert_layer_close_btn").setVisible(False)

def hide_pb(main_window,this_layer):
	get_el_by_id(main_window,"pb_layer").hide()
	get_el_by_id(main_window,this_layer).show()

def task_alert(main_window,this_layer,textval):
	get_el_by_id(main_window,"pb_layer_inp_layer").setText(this_layer)
	get_el_by_id(main_window,"pb_layer_alert_layer_textarea").clear()
	get_el_by_id(main_window,"pb_layer_alert_layer_textarea").insertPlainText(textval)
	get_el_by_id(main_window,this_layer).hide()
	get_el_by_id(main_window,"pb_layer").show()
	get_el_by_id(main_window,"pb_layer_alert_layer_pb_text").setVisible(False)
	get_el_by_id(main_window,"pb_layer_alert_layer_textarea").setVisible(True)
	get_el_by_id(main_window,"pb_layer_alert_layer_close_btn").setVisible(True)
