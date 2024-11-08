/* Add to the end before the last } this */

#ifdef ENABLE_DESTORY_ITEM
	PyModule_AddIntConstant(poModule, "ENABLE_DESTORY_ITEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_DESTORY_ITEM", 0);
#endif