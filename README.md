HelpSet
=======

A Basic Library and REST wrapper for basic Set Implementation


HelpSet Python Library
======================

A Basic Python Library for customized set functions

Following are the functions for a HelpSet
1. Create 
---------
hs = HelpSet([2,4,32,23,2])

2.Add member to set
--------------------
hs.add(3)

3.Remove from Set
------------------
hs.remove(3)

4.Union of Set
---------------
This returns all the elements from two sets with elemination of duplicates
hs1 = HelpSet([23,2,67,34])
hs.union(hs2)

5.Intersection of Set
---------------
This returns all the common elements from two sets
hs1 = HelpSet([23,2,67,34])
hs.intersect(hs2)

4.Difference of Set
---------------
This returns all the elements from set 1 which is not present in set 2
hs2 = HelpSet([23,2,67,34])
hs1.union(hs2)

5.List the elements of set
--------------------------
hs.listSet()

6. Delete a Set
--------------------------
This makes elements of a Set Empty




HelpSet REST API Wrapper
==========================
This REST API wrapper for helpset provides REST API calls for some basic operations of set 
It is assumed that server has kept two default sets stored with id = 1 and id = 2

Routes
----------

1. Route : /v1/helpshift/sets/create
   Methods : POST
   Required Params: values (values in a set separated by ,)

2. /v1/helpshift/sets/delete/<int:set_id>
   Methods : GET
   Required Params: set_id

3. /v1/helpshift/sets/display/<int:set_id>
   Methods : GET
   Required Params: set_id

4. /v1/helpshift/sets/add/<int:set_id>
   Methods : POST
   Required Params: member , set_id

5. /v1/helpshift/sets/union/<int:set_id1>/<int:set_id2>
   Methods : GET
   Required Params: set_id1 , set_id2

6. /v1/helpshift/sets/intersect/<int:set_id1>/<int:set_id2>
   Methods : GET
   Required Params: set_id1 , set_id2

7. /v1/helpshift/sets/cardinality/<int:set_id>
   Methods : GET
   Required Params: set_id

8. /v1/helpshift/sets/remove/<int:set_id>/<member>
   Methods : GET
   Required Params: member , set_id 

7. /v1/helpshift/sets/difference/<int:set_id1>/<int:set_id2>
   Methods : GET
   Required Params: set_id1 , set_id2