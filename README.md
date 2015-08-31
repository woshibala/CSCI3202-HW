# Song_CSCI3202_Assignment1
This is my first assignment in the course 'Introduction to Artificial Intelligence'. THere are five questions should be implement by Pyhton:

1. Implement	a	queue using	the	python	queue	module.	Your	queue	should	
handle	integers	only.
2. Implement	a	stack using	a	list	to	store	the	stack	data.	The	stack	should	be	
implemented	as	a	class	with	at	least	three	methods:
a. push(integer)	
b. pop()
c. checkSize()
3. Implement	a	binary	tree class.	The	tree	should	be	made	up	of	nodes,	which	
are	also	implemented	as	a	class.	The	tree	should	have	a	root	node.	Each	node
in	the	tree has	four	properties:
a. integer key
b. left child
c. right	child
d. parent.	
Your	tree	class	should	have	methods	to	add	a	node,	delete	a	node,	and	print	
the	key	values of	the	nodes.	The	specific	add,	delete,	and	print	functionality	is	
as	follows:
e. add(value,	parentValue)
i. value is	the	key	value	for	the	new	node	and	parentValue is	the	
key	value	of	the	parent.	If	the	parentValue is found	in	the	tree,	
then:
1. add	the	new	node	as	the	left	child	if	the	parent	has	no	
children.
2. add	the	new	node	as	the	right	child	if	the	parent	has	a	
left	child	only.
3. Don’t	add	the	node	if	the	parent	already	has	two	
children.	Print	a	message,	“Parent	has	two children,	
node	not	added”.
4. if	parentValue is	not	found	in	the	tree,	then	print	a	
message,	“Parent	not	found”.
f. delete(value)
i. For	the	delete	operation,	you	only	need	to	delete	nodes	that	
don’t	have	any	children.	
1. If	a	node	has	1	or	2	children,	print	a	message,	“Node	not	
deleted,	has	children”.	
2. If	the	node	is	not	found,	print	a	message,	“Node	not	
found.”
g. print()
i. For	the	print	operation,	print	the	parent	key	value	and	then	the
key values	of	the	children.	This	is	a	pre-order	traversal.
4. Implement	a	graph class	for	an	unweighted	graph	using	a	dictionary	to	store	
the	graph	data.	Each	vertex	in	the	graph	has	an integer	key	value	and	a	list	of	
adjacent	vertices.	Your	class	should	include	the	following	methods:
a. addVertex(value)
i. This	method	first	checks	that	the	vertex	value	doesn’t	already	
exist	in	the	graph,	and	then	adds	it	to	the	graph.	If	the	vertex	is	
already	in	the	graph,	print	a	message,	“Vertex	already	exists”.
b. addEdge(value1,	value2)
i. This	method	takes	the	key	values	of	two	vertices	in	the	graph	
and	adds	an	edge	between	them.	If	one	or	both	of	the	vertices	
don’t	exist	in	the	graph,	the	method	should	print	a	message,	
“One	or	more	vertices	not	found.”
c. findVertex(value)
i. This	method	takes	the	key	value	of	the	vertex	to	search	for,	and	
if	it’s	found	in	the	graph,	print	the	key	values	of	its	adjacent	
vertices.
5. Write	the	code	to	test your	data	structures	in	your	LastName_Assignment1.py	
file.	The	test	code should	clearly	show	which	data	structure	is	being	tested	
the	methods	being	called,	the	arguments	to	the	method,	and	the	state	of	the	
data	structure	after	the	operation. Your	test	code	should	also	be	well	
documented	so	that	the	grader	can	easily	see	what	you’ve	done.
a. Testing	the	queue:
i. Add	at	least	10	integers	to	the	queue	and	then	dequeue	them	
and	print	their	values	in	the	order	they	are	dequeued.
b. Testing	the	stack:
i. Add	at	least	10	integers	to	the	stack	and	then	pop	the	values	
and	print	their	values	in	the	order	they	are	popped.
c. Testing	the	tree:
i. Add	at	least	10	integers	as	nodes	to	the	tree.
ii. Print	the	tree.
iii. Delete	at	least	2	integers	from	the	tree.
iv. Print	the	tree.
d. Testing	the	graph:
i. Add	at	least	10	integers	as	vertices	to	the	graph.
ii. Add	at	least	20	edges	to	the	graph.
iii. Find	5	vertices	in	the	graph.
