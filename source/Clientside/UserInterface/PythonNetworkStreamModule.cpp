/* search */
PyObject* netSendItemDropPacket(PyObject* poSelf, PyObject* poArgs)
{
	[   ]
}

/* add below */
#ifdef ENABLE_DESTORY_ITEM
PyObject* netSendItemDestroyPacket(PyObject* poSelf, PyObject* poArgs)
{
	TItemPos Cell;

	if (!PyTuple_GetInteger(poArgs, 0, &Cell.cell))
		return Py_BuildException();
	CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
	rkNetStream.SendItemDestroyPacket(Cell);
	return Py_BuildNone();
}
#endif

/* search */
		{ "SendItemDropPacketNew",				netSendItemDropPacketNew,				METH_VARARGS },

/* add below */
#ifdef ENABLE_DESTORY_ITEM
		{ "SendItemDestroyPacket",				netSendItemDestroyPacket,				METH_VARARGS },
#endif