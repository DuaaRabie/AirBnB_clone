# Web Static:
## task0:
to align in footer to bottom we could use different ways:
- using (position: absolute; bottom: 0;) this will remove the footer from the normal document flow
and with it to align the text we use (horizontally => text-align: center) and
(vertically => line-height: like footer height)
- The other way, the one I used, prefered it to keep the document flow using flexbox for body and footer,to set to bottom (min-height on body and margin-top on footer) and to center (vertically => align-items, horizontally => justify-content)
