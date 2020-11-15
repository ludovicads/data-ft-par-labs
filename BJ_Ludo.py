{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Do you want to play? yes\n",
      "Dealer has '?' and  4\n",
      "You have  [7, 7]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "import random\n",
    "\n",
    "# Define the a function to play the game\n",
    "def game():\n",
    "\n",
    "# Declare empty lists to append the dealer and player cards\n",
    "    dealer_cards = []\n",
    "    player_cards = []\n",
    "    \n",
    "# Declare a list with the player actions (\"hit: ask another card\" or \"stay: stop with 2 cards \")\n",
    "    hit_stay = [\"hit\", \"stay\"]\n",
    "    \n",
    "# Define a while loop that iterates until the dealer has 2 cards\n",
    "    while len(dealer_cards) !=2:\n",
    "        dealer_cards.append(random.randint(1,11))\n",
    "        if len(dealer_cards) == 2:\n",
    "            print(\"Dealer has '?' and \", dealer_cards[1])\n",
    "    \n",
    "# Define a while loop that iterates until the player has 2 cards           \n",
    "    while len(player_cards) !=2:\n",
    "        player_cards.append(random.randint(1,11))\n",
    "        if len(player_cards) == 2:\n",
    "            print(\"You have \", player_cards)   \n",
    "            \n",
    "# Define a logic condition to finish the game:  if the dealers cards count =21 (\"Blackjack\") or >21 (\"Bust\")      \n",
    "    if sum(dealer_cards) == 21:\n",
    "        print(\"Dealer has BLACK JACK!\")\n",
    "        play_game()\n",
    "    elif sum(dealer_cards) > 21:\n",
    "        print(\"Dealer Bust!\")\n",
    "        play_game()\n",
    "        \n",
    "# Define a while loop that iterates until the player has 21.\n",
    "## Add Error Handling: in case the answer is wrong the questions is repeated \n",
    "### Define a Logic Condition to: repeat the question, hit or stay \n",
    "    while sum(player_cards) < 21:\n",
    "        action_taken = str(input(\"\\nStay or Hit?\"))\n",
    "        action_taken = action_taken.lower()\n",
    "        if action_taken not in hit_stay:\n",
    "            print(\"!!Please choose 'Stay' or 'Hit'\")\n",
    "        elif action_taken == \"hit\":\n",
    "            player_cards.append(random.randint(1,11))\n",
    "            print(\"You have \", player_cards)\n",
    "        else:\n",
    "            print(f\"\\nDealer has {dealer_cards} for a total of: {sum(dealer_cards)}.\")  \n",
    "            print(f\"You have {player_cards} for a total of: {sum(player_cards)}.\")\n",
    "            if sum(dealer_cards) > sum(player_cards):\n",
    "                print(\"dealer wins!\")\n",
    "                play_game()\n",
    "            else:\n",
    "                print(\"you win!\")\n",
    "                play_game()\n",
    "                break\n",
    "                \n",
    "# Define Logic Condition to finish the game if the player cards count>21 (\" Bust\") or =21 (\"Blackjack\")       \n",
    "    if sum(player_cards) > 21:\n",
    "        print(\"Bust!\")\n",
    "        play_game()\n",
    "    elif sum(player_cards) == 21:\n",
    "        print(\"BLACKJACK!! WINNER!!!\")\n",
    "        play_game()\n",
    "        \n",
    "# Define a function to ask to player if they want to play the game or not \n",
    "## Add Error Handling\n",
    "def play_game():\n",
    "    response = [\"yes\", \"no\"]\n",
    "    play = str(input(\"\\nDo you want to play? \"))\n",
    "    play = play.lower()\n",
    "    while play not in response:\n",
    "        play = input(\"Please repond yes or no, dont be awkward.\")\n",
    "    if play == \"yes\":\n",
    "        game()\n",
    "    else:\n",
    "        print(\"\\nTHANK BYE. Save your money\")\n",
    "   \n",
    "play_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
