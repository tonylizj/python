/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
  }
}

const reverseList = (head: ListNode | null): ListNode | null => {
  if (head === null || head.next === null) return head;
  const ret = reverseList(head.next);
  let it = ret;
  while (it.next !== null) {
    it = it.next
  }
  it.next = head;
  it.next.next = null;
  return ret;
};

const test1 = null;
console.log(reverseList(test1));
const test2 = new ListNode(2, null);
console.log(reverseList(test2));
const test3 = new ListNode(3, new ListNode(-1, null));
console.log(reverseList(test3));
const test4 = new ListNode(4, new ListNode(-1, new ListNode(-2, null)));
console.log(reverseList(test4));
