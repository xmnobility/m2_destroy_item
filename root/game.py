# Search
				itemDropQuestionDialog = uiCommon.QuestionDialog()

# Replace like this
				if app.ENABLE_DESTORY_ITEM:
					itemDropQuestionDialog = uiCommon.QuestionDialogItem()
				else:
					itemDropQuestionDialog = uiCommon.QuestionDialog()
					
# Search
				itemDropQuestionDialog.SetAcceptEvent(lambda arg=True: self.RequestDropItem(arg))

# Add below
				if app.ENABLE_DESTORY_ITEM:
					itemDropQuestionDialog.SetDestroyEvent(lambda arg=TRUE: self.RequestDestroyItem(arg))

# Search
	def RequestDropItem(self, answer):
		if not self.itemDropQuestionDialog:
			return

		if answer:
			dropType = self.itemDropQuestionDialog.dropType
			dropCount = self.itemDropQuestionDialog.dropCount
			dropNumber = self.itemDropQuestionDialog.dropNumber

			if player.SLOT_TYPE_INVENTORY == dropType:
				if dropNumber == player.ITEM_MONEY:
					net.SendGoldDropPacketNew(dropCount)
					snd.PlaySound("sound/ui/money.wav")
				else:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP
			elif player.SLOT_TYPE_DRAGON_SOUL_INVENTORY == dropType:
					# PRIVATESHOP_DISABLE_ITEM_DROP
					self.__SendDropItemPacket(dropNumber, dropCount, player.DRAGON_SOUL_INVENTORY)
					# END_OF_PRIVATESHOP_DISABLE_ITEM_DROP

		self.itemDropQuestionDialog.Close()
		self.itemDropQuestionDialog = None

		constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)

# Add below
	if app.ENABLE_DESTORY_ITEM:
		def RequestDestroyItem(self, answer):
			if not self.itemDropQuestionDialog:
				return
			if answer:
				dropType = self.itemDropQuestionDialog.dropType
				dropNumber = self.itemDropQuestionDialog.dropNumber
				if player.SLOT_TYPE_INVENTORY == dropType:
					if dropNumber == player.ITEM_MONEY:
						return
					else:
						self.__SendDestroyItemPacket(dropNumber)
		
			self.itemDropQuestionDialog.Close()
			self.itemDropQuestionDialog = None
			constInfo.SET_ITEM_DROP_QUESTION_DIALOG_STATUS(0)
			

# Search
	# PRIVATESHOP_DISABLE_ITEM_DROP
	def __SendDropItemPacket(self, itemVNum, itemCount, itemInvenType = player.INVENTORY):
		if uiPrivateShopBuilder.IsBuildingPrivateShop():
			chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
			return

		net.SendItemDropPacketNew(itemInvenType, itemVNum, itemCount)

# Add below
	if app.ENABLE_DESTORY_ITEM:
		def __SendDestroyItemPacket(self, itemVNum, itemInvenType = player.INVENTORY):
			if uiPrivateShopBuilder.IsBuildingPrivateShop():
				chat.AppendChat(chat.CHAT_TYPE_INFO, localeInfo.DROP_ITEM_FAILURE_PRIVATE_SHOP)
				return
			net.SendItemDestroyPacket(itemVNum)