# Copyright (c) 2022 Noah Rahm

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.

#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.

#     3. The names of Correct Syntax and Noah Rahm may not be used to endorse
#        or promote products derived from this software without specific prior
#        written permission.       

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


TAX_RATE = 8.0
OUTPUT_FILEPATH = "transactions.txt"


def main():
    i = 0
    items = []
    transactions = {}
    transaction_finished = False

    while transaction_finished is not True:
        # Get each item
        item_name = str(input("ITEM: "))
        item_price = float(input("PRICE: $"))

        items.append((item_name, item_price))
        transactions[i] = items

        # Complete the transaction
        finished = str(input("\nDone entering items? (y/n)"))
        if finished == "y":
            transaction_finished = True

            # Write items to file
            items_string = "\n---\n{}\n".format(transactions[i])
            with open(OUTPUT_FILEPATH, "a") as file:
                file.write(items_string)
            
            # Sum items to get subtotal
            sum = 0.00
            for item in transactions[i]:
                sum = sum + item[1]

            print("\n------------------")
            print("Subtotal: ${}".format(round(sum, 2)))

            # Calculate taxes
            taxes = sum / TAX_RATE

            # Calculate total
            total = round(sum + taxes, 2)
            print("TOTAL: ${}".format(total))
            print("------------------")

            # Get the amount given
            given = float(input("How much were you given? $"))
            while given < total:
                print("Invalid! The customer didn't give you enough.")
                given = float(input("How much were you given? $"))

            # Calculate the change
            change = round(given - total, 2)

            print("\n------------------------")
            print("CHANGE: ${}".format(change))
            print("------------------------")

            # Write total to file
            total_string = "\nTOTAL: {}\n".format(total)
            with open(OUTPUT_FILEPATH, "a") as file:
                file.write(total_string)

            print("Transaction complete!")
        i += 1


if __name__ == "__main__":
    main()
