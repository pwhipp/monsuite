Store
=====

A store is needed for persistent data. This will ideally be workable as a shared ledger.
All values are json with well known fields id, type - type may be undefined.

store = Store(path)

store.put(id, value, timeout=None) -> None, raises: Locked
   timeout of None will retry
store.get(id) -> json object, raises: DoesNotExist
store.delete(id) -> None, raises: DoesNotExist
store.subscribe(id, function) -> unsubscribe function, raises: DoesNotExist
store.block(function, timeout=None, may_write=True) -> value of function, raises: any

store.computed(id, function, types, force=False) -> json object (ret value of function)
   creates block, uses get subscription for cache invalidation.
   Once done, store.get will work. object type is 'computed'.

signals
   put.subscribe(function) -> unsubscribe function
      function called with (old, new)
   get.subscribe(function) -> unsubscribe function
      function called with (obj)
