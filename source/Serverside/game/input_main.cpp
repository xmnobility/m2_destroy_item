/* search */
void CInputMain::ItemDrop2(LPCHARACTER ch, const char * data)
{
    [...]
}

/* add below */
#ifdef ENABLE_DESTORY_ITEM
void CInputMain::ItemDestroy(LPCHARACTER ch, const char * data)
{
	struct command_item_destroy * pinfo = (struct command_item_destroy *) data;
	if (ch)
		ch->DestroyItem(pinfo->Cell);
}
#endif

/* search */
		case HEADER_CG_ITEM_DROP2:
			if (!ch->IsObserverMode())
				ItemDrop2(ch, c_pData);
			break;

/* add below */
#ifdef ENABLE_DESTORY_ITEM
		case HEADER_CG_ITEM_DESTROY:
			if (!ch->IsObserverMode())
				ItemDestroy(ch, c_pData);
		break;
#endif