/* search */
		bool SendItemDropPacketNew(TItemPos pos, DWORD elk, DWORD count);

/* add below */
#ifdef ENABLE_DESTORY_ITEM
		bool SendItemDestroyPacket(TItemPos pos);
#endif