# Contribution Convention
Here's all you need to know to contribute to this repository. For beginners, here's what you need to have before creating a Pull Request to this repo.

1. Fork this repository.
2. Create a new branch, using our [branch naming convention](#branch-naming-convention).
3. Add your contents [Not yours? Read Here.](#credit-source).
4. Send us a Pull Request. Write a description that contains "what you do in this Pull Request".

Failing to follow this convention might slow your merging process or your request(s) being rejected/closed.

For any questions related to this Contribution Convention, please create a new Issue and reference this Convention.

## Having issues?
If you have any issues using the resource, please find any issue that might have been resolved. If it is not there, create it and fill in the form.

## Branch Naming Convention
After you have forked this repo (or directly commit to this repo), create a new branch that matches our branch name convention.

You shall use one of these prefix to name your branch.
- `typos/<language-ISO-code>/<word-pack-name>` for word typos-related Pull Request.
- `content/<language-ISO-code>/<word-pack-name>` for adding more words to the repo.
- `patch/<issue-number>/<word-pack-name>` for any Python script patches and tweaks.
- `chore/` for editing any docs-based files (e.g. this CONTRIBUTING.md file)

For example, if you want to add wordlist for Adults, create your branch as `content/en-en/adults` and start adding contents!

For `<language-ISO-code>`, follow [ISO-standard language code (ISO 639-1:2002)](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) (e.g. `en-EN` for Standard English, `zh-hk` for Hongkong Chinese)

For `<word-pack-name>`, use [lowercase-kebab-case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles) (e.g. `duos-nsfw`)

If you have any questions, feel free to create a new issue and reference this heading.

## Add new content
To start adding wordlist, create these files under `wordlist/<language-ISO-code>/<word-pack-name>` :
- `wordlist.txt` for [word list](#word-list).
- `README.md` for [credit source and word list description](#credit-source).

### Word list
For a new wordlist, add your word in the `wordlist.txt` **as line separated**.<br/>Word list that is not line separated will be automatically closed.

And each word must follow this guideline:
- No typos are allowed.
- Encode file using an appropriate file encoding (e.g. UTF-8).

and this covention:
- Each word **is a word. Not a sentence.**
- Must contains **only one ISO language code**.
- Wordlist **does not contain duplicate** based on each language's [duplication guidelines](#duplication-guidelines).
- Check that your wordlist is **not a duplicate to *pending wordlist Pull Request* or *existing wordlist*.**
- Same word that can be exchangable is considered duplicates.

This convention list is born-to-be exploited. If you feel like your word list should not follow this convention or feel like this convention is a flaw, feel free to reply and explains why you think it shouldn't follow the convention.

### Credit Source
For contents that you scrapped from any source, you must add the source that you brought from in `README.md`.

In that file, add a URL and/or description on where you scrapped these words from.
Add any description you feel like to.

## Send us a Pull Request
Create us a Pull Request! Just complete the Pull Request form and start creating a PR.

You might be required to edit your request or stand-your-ground at anytime.

---

## Duplication Guidelines
### Germanic Languages
*Applies to : English, French, German, Dutch, Swedish, Danish, Norwegian, Scots, Icelandic*
- Is in either Capital Case or Lower Case.
- Avoid using language grammatical information (eg. gender, person, number, tense, aspect, mood, voice, etc.) in each word.
    - If the word must contain a gender-specific word, use a widely used/accepts gender or use neutral/neuter gender instead.
    - Use Present Simple Tense for time-specific word.
- Strongly avoid using Non-finite verb (e.g. infinitives, participles, gerunds).
- Part of speech (e.g. Noun, Verb, Adjective) form counts as the same word.

### The rest of the world
We still have no language guidelines, until you turned in! If you feel like to, you can create a Pull Request and suggests.
