# Search
class QuestionDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.__CreateDialog()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __CreateDialog(self):
		pyScrLoader = ui.PythonScriptLoader()
		pyScrLoader.LoadScriptFile(self, "uiscript/questiondialog.py")

		self.board = self.GetChild("board")
		self.textLine = self.GetChild("message")
		self.acceptButton = self.GetChild("accept")
		self.cancelButton = self.GetChild("cancel")

	def Open(self):
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def Close(self):
		self.Hide()

	def SetWidth(self, width):
		height = self.GetHeight()
		self.SetSize(width, height)
		self.board.SetSize(width, height)
		self.SetCenterPosition()
		self.UpdateRect()

	def SAFE_SetAcceptEvent(self, event):
		self.acceptButton.SAFE_SetEvent(event)

	def SAFE_SetCancelEvent(self, event):
		self.cancelButton.SAFE_SetEvent(event)

	def SetAcceptEvent(self, event):
		self.acceptButton.SetEvent(event)

	def SetCancelEvent(self, event):
		self.cancelButton.SetEvent(event)

	def SetText(self, text):
		self.textLine.SetText(text)

	def SetAcceptText(self, text):
		self.acceptButton.SetText(text)

	def SetCancelText(self, text):
		self.cancelButton.SetText(text)

	def OnPressEscapeKey(self):
		self.Close()
		return TRUE

# Add above
if app.ENABLE_DESTORY_ITEM:
	class QuestionDialogItem(ui.ScriptWindow):
		def __init__(self):
			ui.ScriptWindow.__init__(self)
			self.__CreateDialog()
		def __del__(self):
			ui.ScriptWindow.__del__(self)
		def __CreateDialog(self):
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/questiondialogitem.py")
			self.board = self.GetChild("board")
			self.textLine = self.GetChild("message")
			self.acceptButton = self.GetChild("accept")
			self.destroyButton = self.GetChild("destroy")
			self.cancelButton = self.GetChild("cancel")
		def Open(self):
			self.SetCenterPosition()
			self.SetTop()
			self.Show()
		def Close(self):
			self.Hide()
		def SetWidth(self, width):
			height = self.GetHeight()
			self.SetSize(width, height)
			self.board.SetSize(width, height)
			self.SetCenterPosition()
			self.UpdateRect()
		def SAFE_SetAcceptEvent(self, event):
			self.acceptButton.SAFE_SetEvent(event)
		def SAFE_SetCancelEvent(self, event):
			self.cancelButton.SAFE_SetEvent(event)
		def SetAcceptEvent(self, event):
			self.acceptButton.SetEvent(event)
		def SetDestroyEvent(self, event):
			self.destroyButton.SetEvent(event)
		def SetCancelEvent(self, event):
			self.cancelButton.SetEvent(event)
		def SetText(self, text):
			self.textLine.SetText(text)
		def SetAcceptText(self, text):
			self.acceptButton.SetText(text)
		def SetCancelText(self, text):
			self.cancelButton.SetText(text)
		def OnPressEscapeKey(self):
			self.Close()
			return TRUE