# Egyptians in AI Research

Website: https://bkhmsi.github.io/egyptians-in-ai/

Welcome to Egyptian in AI, a website dedicated to showcasing the profiles of prominent Egyptian researchers in the field of artificial intelligence. 

If you think that someone is missing from our list of featured researchers, we welcome contributions from the community. To be considered for inclusion, the only criteria is that the individual must have an h-index of 5 or higher, as recorded on their Google Scholar profile. You can submit your suggestion by filling out [this form](https://docs.google.com/forms/d/e/1FAIpQLSdLaYBQyOzI5gnlGzwOki3b1TJtFjLUeHUKxkGtXQDhHdSreg/viewform?usp=sf_link), or request updates for existing profiles.

We hope that you find our website informative and inspiring, and we invite you to explore the profiles of our featured researchers to learn more about their work.

## Other `X in Y` Websites:
- [Moroccans in AI Research](https://mair.ma)
- [Pakistanis in AI Research](https://ahmadmustafaanis.github.io/Pakistanis-in-ai/)

## Steps to Create Your Own `X in Y` Website

1. Fork this repository: 
Click the "Fork" button at the top right of this repository's page to create your own copy.
2. Replace data in `./src/assets/researchers_en.json`:
Navigate to the `./src/assets` directory and locate the `researchers_en.json` file. Replace the existing data with profiles you want to feature, following the same JSON structure.
3. Replace all metadata and details specific to this website:
In various places (like navigation bar, metadata, and the Google Form link), update all instances of website-specific information to your own. Make sure to modify links, headers, and other details according to your website's needs.
4. Run your website locally using `ng serve`:
Open a terminal, navigate to your project's root directory, and run `ng serve`. This will start a local development server, and you can access your website by opening your browser and going to `http://localhost:4200`.
5. Build the website:
After verifying everything works locally, build your website using the following command in your terminal:
    ```bash
    ng build --configuration production --base-href {{website_url}}
    ```
    Replace `{{website_url}}` with the actual URL where your website will be hosted, such as `https://bkhmsi.github.io/egyptians-in-ai/`.

6. Copy the built files:
Locate the `dist` folder in your project's directory. Inside `dist`, you'll find a folder named after your website (e.g., egyptians-in-ai). Copy this folder and move it to the root directory of your forked repository. Rename the copied folder to `docs`.

7. Configure GitHub Pages:
- Open your forked repository on GitHub.
- Go to the "Settings" tab.
- Scroll down to the "GitHub Pages" section.
- Under "Source," choose the docs folder from the dropdown.
- Save the changes.
You can reference this [GitHub article](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) for more details.
8. Reach out to me:
Reach out with the link to your deployed website so I can include it in the list of `X in Y` websites.

Remember, if you encounter any issues during the process, don't hesitate to ask for help!


## Update Website 

1. Download the spreadsheet with new entries as `researchers.csv`
2. Run `scripts/populate.py`, this will create two spreadsheets `researchers_new.json` and `researchers_update.json`
3. Append valid entries in `researchers_new.json` to `researchers_en.json`
4. Run `scripts/google_scholar.py` to update h-index values that will create a new file `researchers_en_new.json`
5. Update entries in `researchers_en_new.json` with valid entries in `researchers_update.json`
6. Rename `researchers_en_new.json` with `researchers_en.json`

## Pre-Build
```
export NODE_OPTIONS=--openssl-legacy-provider
```