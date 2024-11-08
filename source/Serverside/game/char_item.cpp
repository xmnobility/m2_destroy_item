/* search */ 
bool CHARACTER::DropItem(TItemPos Cell, BYTE bCount)

/* add below */
#ifdef ENABLE_DESTORY_ITEM
bool CHARACTER::DestroyItem(TItemPos Cell)
{
	LPITEM item = NULL;
	if (!CanHandleItem())
	{
		if (NULL != DragonSoul_RefineWindow_GetOpener())
			ChatPacket(CHAT_TYPE_INFO, LC_TEXT("°*E*A￠A≫ ¿￢ ≫oAA¿¡¼*´A ¾ÆAIAUA≫ ¿A±æ ¼o ¾ø½A´I´U."));
		return false;
	}
	if (IsDead())
		return false;
	if (!IsValidItemPosition(Cell) || !(item = GetItem(Cell)))
		return false;
	if (item->IsExchanging())
		return false;
	if (true == item->isLocked())
		return false;
	if (quest::CQuestManager::instance().GetPCForce(GetPlayerID())->IsRunning() == true)
		return false;
	if (item->GetCount() <= 0)
		return false;
	SyncQuickslot(QUICKSLOT_TYPE_ITEM, Cell.cell, 255);
	ITEM_MANAGER::instance().RemoveItem(item);
	ChatPacket(CHAT_TYPE_INFO, LC_TEXT("Ai sters %s ."), item->GetName());
	return true;
}
#endif