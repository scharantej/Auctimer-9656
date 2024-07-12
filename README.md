## Flask Application Design for Auction System

### HTML Files

- **index.html**:
   - Homepage of the application.
   - Contains the user interface for placing bids.
   - Includes a countdown timer that displays the remaining time to place a bid.
- **success.html**:
   - Displayed when a bid is successfully placed within the time limit.
- **failure.html**:
   - Displayed when a bid is not placed within the time limit or if the bid amount is not valid.

### Routes

- **GET /**:
   - Renders the `index.html` page.
- **POST /bid**:
   - Receives the bid amount and time remaining as parameters.
   - Checks if the bid is valid (within the time limit and amount is greater than zero).
   - If valid, saves the bid information and redirects to `success.html`.
   - If not valid, redirects to `failure.html`.