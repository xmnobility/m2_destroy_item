/* search */
HEADER_CG_ITEM_DROP2			= 20,

/* add below */
#ifdef ENABLE_DESTORY_ITEM
  HEADER_CG_ITEM_DESTROY			= 21,
#endif

/* search */
typedef struct command_item_drop2
{
	[...]
} TPacketCGItemDrop2;

/* add below */
#ifdef ENABLE_DESTORY_ITEM
typedef struct command_item_destroy
{
	BYTE		header;
	TItemPos	Cell;
} TPacketCGItemDestroy;
#endif

/* continue as you have -> = 21, */