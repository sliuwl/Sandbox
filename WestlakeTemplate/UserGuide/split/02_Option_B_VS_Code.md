# Option B: Visual Studio Code (VS Code) Recommended

- Download correct version of TeX according to your system at [https://www.latex-project.org/get/](https://www.latex-project.org/get/) (if you never did this before):

  ![Download TeX](../images/image4.png)

- Use Compiler (like TeXShop on Mac) as you wish or if you are using VS Code, an easy way is compile `.tex` in VS Code by first downloading the Extension **LaTeX Workshop**:

  ![LaTeX Workshop Extension](../images/image5.png)

- Decompress the `.zip` and import into VS Code:

  ![Decompress zip and import into VS Code](../images/image6.png)

---

## Q1: How to get proposal.tex compiled into proposal.pdf

- Manage your reference in the `.bib` file in the folder:

  ![Manage reference in proposal.bib](../images/image7.png)

- Compile by calling following lines (one by one) in terminal:

  ```bash
  xelatex proposal
  ```

  ![xelatex proposal](../images/image8.png)

  ```bash
  biber proposal
  ```

  ![biber proposal](../images/image9.png)

  ```bash
  xelatex proposal
  ```

  ![xelatex proposal final](../images/image10.png)

- You’ll see the compiled `.pdf` file. Each time if you need an update, call those three commands above again.

---

## Q2: How to get thesis.tex compiled into thesis.pdf

**Summary:** Similar to compiling `proposal.tex`, manage your reference in `thesis.bib`, and call three commands in TERMINAL one by one. Only difference is that you need to change **`biber proposal`** to **`bibtex thesis`**. (Short reason if you wish to know: in proposal we have two local references, one after the literature review section, the other after the real proposal section, to reach that goal we use another engine for reference management, resulting in this change).

- Manage your reference in the `.bib` file in the folder:

  ![Manage reference in thesis.bib](../images/image11.png)

- Go to the proper Thesis folder in terminal:
  - Call `cd ..` to go back to parent folder
  - Call `cd Thesis` to go to the target Thesis folder

  ![Terminal cd to Thesis folder](../images/image12.png)

- Compile by calling following lines (one by one) in terminal:

  ```bash
  xelatex thesis
  ```

  ![xelatex thesis](../images/image13.png)

  ```bash
  bibtex thesis
  ```

  ![bibtex thesis](../images/image14.png)

  ```bash
  xelatex thesis
  ```

  ![xelatex thesis final](../images/image15.png)

- Enjoy your masterpiece or improve your work to make it masterpiece by calling those three commands above again when you need an update.
