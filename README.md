# Supermarket Kata

This is a variation of a popular kata described in http://codekata.com/kata/kata01-supermarket-pricing/. The aim of the exercise is to build automated tests for this code, refactor it, and add a new feature.

The supermarket has a catalog with different types of products (rice, apples, milk, toothbrushes,...). Each product has a price, and the total price of the shopping cart is the total of all the prices of the items. You get a receipt that details the items you've bought, the total price and any discounts that were applied.


# Requirements:

## Shopping Cart
- A new shopping cart has 0 items
- After adding an item, shopping cart contains 1 item
- After removing the item, shopping cart is empty
- When trying to remove an item from empty shopping cart, throw an error
- After adding 2 items, shopping cart contains 2 items
- After adding 2 items and removing 1, shopping cart contains only the item that wasn't removed

## Price
- An item has a name and a price
- When shopping cart contains 1 item, total price is price of that item
- When shopping cart contains more items, total price is sum of items' price

## Receipt
- When printing the receipt, show a list of items and their price
- The last line should contain the total price
- Items with the same name are grouped (e.g. 3 Carrots @ 0,40      EUR 1,20)

## Discount
- If there are discounts applicable to an item, the receipt should contain
  an extra line with the discount  
  (e.g. 10% discount = EUR -0.12)
- The receipt should show the total discount after the total price
- Items can have a percentage discount, meaning a certain percentage is
  substracted from the price
- Items can have a "buy 2 get 1 free" discount, which applies when there
  are three items of this name present in the shopping cart
- Items can have a "buy x get y free" discount, which applies when there
  are x + y items of this name present in the shopping cart
- Items can have a "x items for price y" discount, which applies when there
  are x items of this name present in the shopping cart

## Grouping
- Items can be part of a group (e.g. a brand or type such as "fresh produce")
- Items from a group can have a percentage discount
- Items can have a discount "buy x from group for price y", which applies when
  there are x items from this group in the shopping cart
- The group discount is printed per item on the receipt as the percentage of the
  discount applicable to this item

## Example

```
Apple                     EUR  0,15
Toilet paper              EUR  1,99
Oranges 
  2 x 0,30                EUR  0,60
Carrots
  3 x 0,40                EUR  1,20
  10% discount            EUR -0,12
Toothpaste
  3 x 4,50                EUR 13,50
  buy 2 get 1 free        EUR -4,50
Pasta sauce
  3 x 2,17                EUR  6,51
  buy 3 for 5,00          EUR -1,51
Macaroni                  EUR  0,98
Bla Shampoo               EUR  2,99
  Fa discount 30%         EUR -0,67
Bla Soap
  2 x 1,50                EUR  3,00
  Fa discount 30%         EUR -0,67
Ack Fresh Deo             EUR  4,20
  Ack 3 for 9,00          EUR -1,30
Ack Shower Gel            EUR  4,99
  Ack 3 for 9,00          EUR -1,55
Ack Power Plus            EUR  3,99
  Ack 3 for 9,00          EUR -1,24


TOTAL                     EUR 32,54 

TOTAL DISCOUNT            EUR 11,56
```
