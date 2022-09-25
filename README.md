# T1A3_Terminal App

## [Link to repository](https://github.com/Dandandan-mo/T1A3-Terminal-App)

## Resources referenced
- [Cowsay 5.0](https://pypi.org/project/cowsay/)
- [Colorama 0.4.5](https://pypi.org/project/colorama/)
- [py_currency_converter 1.2.0](https://pypi.org/project/py-currency-converter/)

## Style guide
This application adhere to the [PEP8 Style Guide for Python Code](https://peps.python.org/pep-0008/) 

## Features
- ### Feature 1: Tracking incomes and expenses
This application prompts users to enter their income and expense transaction details in different cateogries. Once user finish entering all the transactions, the app calculates the remaining balance and display a transaction summary with all transaction details. By selecting the different income or expense category, users can also view transaction details and subtotal in different categories.
- ### Feature 2: Customise categories
When users are entering income or expense transactions, they can customise a cateogry if none of the income or expense categories listed in the app is suitable. This helps users accurately track their income or expenses. When choosing the category by entering their corresponding number, users can enter a number not listed (not including 0) and the application will then prompt users to name the new category. The new category is then added to the income / expense category list and displayed on the screen with all the other default options.
- ### Feature 3: Setting up a saving goal
Users can enter their saving goal (a number) and the app will compare the goal with the remaining balance after all the incomes and expenses are entered. If the user achieve their saving goal, a congratulation is displayed, otherwise the app tells the users how much they still need to save in order to achieve the goal.
- ### Feature 4: Currency conversion
The end user of this application are people with additional incomes or expenses in other currencies (such as international students or working visa holders). In some occasions, these users need to transfer their money abroad or have additional incomes in other currencies from other countries, which is when exchange rates are taken into consideration when budgets are being managed. Therefore, the last feature of this app enables users to convert their Australian dollar into another currency. They have the options to convert their total remaining balance, their saving goal, or enter a new amount for conversion. Users can enter the ISO currency code and the application will display the amount coverted into the corresponding currency.
## Implementation plan
The project management platform used for the development of this application is Trello ([click to view the Trello board](https://trello.com/invite/b/DzCCyjbo/537cd16c934e3e696965d6dfb5955c65/t1a3-terminal-app-budget-app)).
![trelloboard](/docs/trelloboard.png)
![feature1](/docs/feature1.png)
![feature2](/docs/feature2.png)
![feature3](/docs/feature3.png)
![feature4](/docs/feature4.png)
## Installation instructions
0. Open your terminal.
1. Clone this app projectfrom git repository by using the following command line instruction:
```bash
git clone https://github.com/Dandandan-mo/T1A3-Terminal-App.git
```
2. Naviate to the 'T1A3-Terminal-App' directory from whatever directory you are currently in:
```bash
cd T1A3-Terminal-App
```
3. Get permission to execute the bash script:
```bash
chmod +x my_wrapper.sh
```
4. Run the bash script with an argument. The argument will depends on the system of your computer.

If you have a Linux system:
```bash
./my_wrapper.sh Linux
```
If you have a MacOS system:
```bash
./my_wrapper.sh MacOS
```
If you have a Windows system:
```bash
./my_wrapper.sh Windows
```
- You need to have python3 installed for the program to run. If not, you will get a prompt to [install python3](https://installpython3.com/).
- You need to have pip installed. Usually it is installed by default. If not, pip will be installed automatically when the bash script runs.
- The application requares three python third-party packages to operate: "cowsay", "colorama", and "py_currency_converter". These packages will be automatically installed in a virtual environment when the bash script runs.

The application will run once all the installations are done. Enjoy!

## Presentation
[vimeo link](https://vimeo.com/753531406)


