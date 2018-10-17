class func(object):
	
	def __init__(self,fm,page,setUIPage):
		self.fm        = fm
		self.page      = page
		self.setUIPage = setUIPage

		self.rig()
		self.update_info()

	def rig(self):
		self.page.sbSensorID.valueChanged.connect(self.update_info)
		self.page.pbGoModule.clicked.connect(self.goModule)

	def update_info(self,ID=None):
		if ID is None:ID = self.page.sbSensorID.value()
		info = self.fm.loadSensorDetails(ID)

		if info is None:
			self.page.leIdentifier.setText("")
			self.page.leType.setText("")
			self.page.leSize.setText("")
			self.page.leChannels.setText("")
			self.page.leManufacturer.setText("")
			self.page.leOnModule.setText("")

		else:
			self.page.leIdentifier.setText(info["identifier"])
			self.page.leType.setText(info["type"])
			self.page.leSize.setText(info["size"])
			self.page.leChannels.setText(info["channels"])
			self.page.leManufacturer.setText(info["manufacturer"])
			self.page.leOnModule.setText(info["onModuleID"])

	def goModule(self):
		ID = self.page.leOnModule.text()
		if len(ID) > 0:
			try:
				ID = int(ID)
			except:
				return
			self.setUIPage('modules',ID=ID)
		else:
			return
	
	def load_kwargs(self,kwargs):
		if 'ID' in kwargs.keys():
			ID = kwargs['ID']
			if not (type(ID) is int):
				raise TypeError("Expected type <int> for ID; got <{}>".format(type(ID)))
			if ID < 0:
				raise ValueError("ID cannot be negative")
			self.page.sbSensorID.setValue(ID)