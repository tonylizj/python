
// made this because JS objects were confusing after C++
// I have no idea if this is how you're supposed to write a deep copy operator btw

class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
  }
  deepCopy(): ListNode {
    if (this.next === null) return new ListNode(this.val, null);
    return new ListNode(this.val, this.deepCopy.bind(this.next)());
  }
}

console.log('Original:                      ', new ListNode(1, new ListNode(2)));
// ListNode { val: 1, next: ListNode { val: 2, next: null } }
console.log('After copying the object and changing the copy\'s list values to 7 and 8 using...\n');

let a = new ListNode(1, new ListNode(2));
let b = a;
b.val = 8;
b.next.val = 9;
console.log('Assignment Operator:           ', a);
// ListNode { val: 8, next: ListNode { val: 9, next: null } }

let c = new ListNode(1, new ListNode(2));
let d = {...c};
d.val = 8;
d.next.val = 9;
console.log('Shallow Copy (Spread Operator):', c);
// ListNode { val: 1, next: ListNode { val: 9, next: null } }

let e = new ListNode(1, new ListNode(2));
let f = e.deepCopy();
f.val = 8;
f.next.val = 9;
console.log('Deep Copy Method:              ', e);
// ListNode { val: 1, next: ListNode { val: 2, next: null } }
