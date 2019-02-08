PAGE_NAME = "view_sensor"
OBJECTTYPE = "sensor"
DEBUG = False

class func(object):
	def __init__(self,fm,page,setUIPage,setSwitchingEnabled):
		self.fm        = fm
		self.page      = page
		self.setUIPage = setUIPage
		self.setMainSwitchingEnabled = setSwitchingEnabled

		self.info = None
		self.mode = 'setup'



	def enforce_mode(mode):
		if not (type(mode) in [str,list]):
			raise ValueError
		def wrapper(function):
			def wrapped_function(self,*args,**kwargs):
				if type(mode) is str:
					valid_mode = self.mode == mode
				elif type(mode) is list:
					valid_mode = self.mode in mode
				else:
					valid_mode = False
				if valid_mode:
					if DEBUG:
						print("page {} with mode {} req {} calling function {} with args {} kwargs {}".format(
							PAGE_NAME,
							self.mode,
							mode,
							function.__name__,
							args,
							kwargs,
							))
					function(self,*args,**kwargs)
				else:
					print("page {} mode is {}, needed {} for function {} with args {} kwargs {}".format(
						PAGE_NAME,
						self.mode,
						mode,
						function.__name__,
						args,
						kwargs,
						))
			return wrapped_function
		return wrapper



	@enforce_mode('setup')
	def setup(self):
		self.rig()
		self.mode = 'view'
		print("{} setup completed".format(PAGE_NAME))
		self.update_info()

	@enforce_mode('setup')
	def rig(self):
		self.page.sbSensorID.valueChanged.connect(self.update_info)
		self.page.pbGoModule.clicked.connect(self.goModule)

		self.page.pbSensorNew.clicked.connect(self.startCreating)
		self.page.pbSensorEdit.clicked.connect(self.startEditing)
		self.page.pbSensorSave.clicked.connect(self.saveEditing)
		self.page.pbSensorCancel.clicked.connect(self.cancelEditing)



	@enforce_mode('view')
	def update_info(self,ID=None,*args,**kwargs):
		if ID is None:ID = self.page.sbSensorID.value()
		self.info = self.fm.loadObjectDetails(OBJECTTYPE,ID)
		self.updateElements(use_info = True)

	@enforce_mode(['view','editing','creating'])
	def updateElements(self,use_info=False):
		if use_info:
			if self.info is None:
				self.page.leIdentifier.setText("")
				self.page.leType.setText("")
				self.page.dsbSize.setValue(-1.0)
				self.page.dsbSize.clear()
				self.page.sbChannels.setValue(-1)
				self.page.sbChannels.clear()
				self.page.leManufacturer.setText("")
				self.page.sbOnModule.setValue(-1)
				self.page.sbOnModule.clear()
			else:
				self.page.leIdentifier.setText(   self.info["identifier"]   )
				self.page.leType.setText(         self.info["type"]         )
				self.page.dsbSize.setValue(       self.info["size"]         )
				self.page.sbChannels.setValue(    self.info["channels"]     )
				self.page.leManufacturer.setText( self.info["manufacturer"] )
				self.page.sbOnModule.setValue(    self.info["onModuleID"]   )

				if self.info["size"]         == -1.0: self.page.dsbSize.clear()
				if self.info["channels"]     == -1  : self.page.sbChannels.clear()
				if self.info["onModuleID"]   == -1  : self.page.sbOnModule.clear()


		self.page.pbSensorNew.setEnabled(    (self.mode == 'view') and     (self.info is None) )
		self.page.pbSensorEdit.setEnabled(   (self.mode == 'view') and not (self.info is None) )
		self.page.pbSensorSave.setEnabled(   self.mode in ['editing','creating'] )
		self.page.pbSensorCancel.setEnabled( self.mode in ['editing','creating'] )

		self.setMainSwitchingEnabled(self.mode == 'view')

		self.page.pbGoModule.setEnabled( (self.mode=='view') and (self.page.sbOnModule.value()>=0) ) 
		self.page.sbSensorID.setEnabled( self.mode=='view' )
		self.page.leIdentifier.setReadOnly(   not (self.mode in ['editing','creating']))
		self.page.leType.setReadOnly(         not (self.mode in ['editing','creating']))
		self.page.dsbSize.setReadOnly(        not (self.mode in ['editing','creating']))
		self.page.sbChannels.setReadOnly(     not (self.mode in ['editing','creating']))
		self.page.leManufacturer.setReadOnly( not (self.mode in ['editing','creating']))
		self.page.sbOnModule.setReadOnly(     not (self.mode in ['editing','creating']))

	@enforce_mode('view')
	def startCreating(self,*args,**kwargs):
		if self.info is None:
			self.mode = 'creating'
			self.updateElements()
		else:
			pass

	@enforce_mode('view')
	def startEditing(self,*args,**kwargs):
		if self.info is None:
			pass
		else:
			self.mode = 'editing'
			self.updateElements()

	@enforce_mode(['editing','creating'])
	def cancelEditing(self,*args,**kwargs):
		self.mode = 'view'
		self.update_info()

	@enforce_mode(['editing','creating'])
	def saveEditing(self,*args,**kwargs):
		ID = self.page.sbSensorID.value()
		details = {
			'identifier'   : str(self.page.leIdentifier.text()),
			'type'         : str(self.page.leType.text()),
			'size'         : self.page.dsbSize.value(),
			'channels'     : self.page.sbChannels.value(),
			'manufacturer' : str(self.page.leManufacturer.text()),
			'onModuleID'   : self.page.sbOnModule.value(),
			}
		new = self.mode == 'creating'
		self.fm.changeObjectDetails(OBJECTTYPE,ID,details,new)
		self.mode = 'view'
		self.update_info()

	@enforce_mode('view')
	def goModule(self,*args,**kwargs):
		ID = self.page.sbOnModule.value()
		if ID >= 0:
			self.setUIPage('modules',ID=ID)
		else:
			return

	@enforce_mode('view')
	def load_kwargs(self,kwargs):
		if 'ID' in kwargs.keys():
			ID = kwargs['ID']
			if not (type(ID) is int):
				raise TypeError("Expected type <int> for ID; got <{}>".format(type(ID)))
			if ID < 0:
				raise ValueError("ID cannot be negative")
			self.page.sbSensorID.setValue(ID)

	@enforce_mode('view')
	def changed_to(self):
		print("changed to {}".format(PAGE_NAME))