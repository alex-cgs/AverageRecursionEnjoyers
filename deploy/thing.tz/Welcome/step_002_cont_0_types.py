import smartpy as sp

tstorage = sp.record(myParameter1 = sp.int, myParameter2 = sp.int).layout(("myParameter1", "myParameter2"))
tparameter = sp.variant(myEntryPoint = sp.int).layout("myEntryPoint")
tprivates = { }
tviews = { }
