class PyIExchangeManageStoreEx : public PyIUnknown
{
public:
MAKE_PYCOM_CTOR(PyIExchangeManageStoreEx);
static PyComTypeObject type;
static IExchangeManageStoreEx *GetI(PyObject *self);
	static PyObject *CreateStoreEntryID2(PyObject *self, PyObject *args);
protected:
	PyIExchangeManageStoreEx(IUnknown *);
	~PyIExchangeManageStoreEx();
};

