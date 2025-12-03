# GitHub Setup Instructions

## Complete Step-by-Step Guide (15 minutes)

### STEP 1: Create Repository on GitHub (2 min)

1. Go to https://github.com/new
2. Fill out:
   ```
   Repository name: psi7-coefficient
   Description: The Heptagonal Coefficient (ψ₇): A universal constant in 7-fold systems
   Public: YES ✓
   Add .gitignore: NO (we have our own)
   Add license: NO (we have three custom licenses)
   Initialize with README: NO (we have our own)
   ```
3. Click **Create Repository**

4. You'll see a page with commands. **Copy the HTTPS URL** from the line that says:
   ```
   git remote add origin https://github.com/YOUR-USERNAME/psi7-coefficient.git
   ```

### STEP 2: Install Git (if needed)

**On Mac:**
```bash
brew install git
```

**On Windows:**
Download from https://git-scm.com/download/win

**On Linux:**
```bash
sudo apt-get install git
```

**Verify:**
```bash
git --version
```

### STEP 3: Configure Git (2 min, one-time)

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Example:
```bash
git config --global user.name "William Banick"
git config --global user.email "william@base7.com"
```

### STEP 4: Download the Repository Files (1 min)

The complete repository is in:
```
/mnt/user-data/outputs/psi7-coefficient-repo/
```

**Download this folder to your computer** (extract the ZIP or copy the folder).

### STEP 5: Initialize and Push (5 min)

Open Terminal/Command Prompt in the repository folder:

```bash
# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: ψ₇ coefficient discovery with validation"

# Add remote (paste YOUR URL from Step 1)
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/psi7-coefficient.git

# Push to GitHub
git push -u origin main
```

### STEP 6: Add GitHub Topics (1 min)

Go to your GitHub repository homepage and scroll down to "About" section.

Click the gear icon and add these topics:
```
heptagonal-geometry
mathematical-discovery
universal-constants
mathematics
physics
geometry
open-science
```

---

## Expected Output

When you run `git push -u origin main`, you should see:

```
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (15/15), 2.34 MiB | 1.23 MiB/s, done.
Total 15 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/YOUR-USERNAME/psi7-coefficient.git
 * [new branch]      main -> main
Branch 'main' is set up to track remote branch 'main' from 'origin'.
```

**Success!** Your repository is now live.

---

## Verify Success

Visit: `https://github.com/YOUR-USERNAME/psi7-coefficient`

You should see:
- ✓ All files visible
- ✓ README.md displaying on the main page
- ✓ Green "Code" button to clone
- ✓ License information showing

---

## Troubleshooting

### "fatal: not a git repository"
**Solution:** Make sure you're in the correct folder:
```bash
cd path/to/psi7-coefficient-repo
pwd  # verify you're in the right place
git init
```

### "fatal: authentication failed"
**Solution:** GitHub now requires personal access tokens instead of passwords.

1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Name it: "git-cli"
4. Check: `repo` (full control of private repositories)
5. Set expiration: 90 days
6. Click "Generate token"
7. **Copy the token**
8. When git asks for password, paste the token instead

### "rejected ... because the remote contains work that you do not have locally"
**Solution:** Pull first:
```bash
git pull origin main --allow-unrelated-histories
git push origin main
```

### "Repository already exists"
**Solution:** Delete the repository on GitHub and create a new one. Then try again.

---

## Next Steps After Launch

### Immediate (Same Day)
- [ ] Verify repository is live
- [ ] Test clone on a different machine: `git clone https://github.com/YOUR-USERNAME/psi7-coefficient.git`

### Within 24 Hours
- [ ] Create arXiv preprint (see ARXIV_SETUP.md)
- [ ] Post on Twitter/Reddit/HackerNews (see SOCIAL_LAUNCH.md)
- [ ] Email to 5 mathematicians (see OUTREACH_TEMPLATES.md)

### Within 1 Week
- [ ] Initial feedback from community
- [ ] Refine papers based on questions
- [ ] Begin peer review submission process

---

## The Repository is Now a Permanent Record

Once pushed to GitHub:
- ✓ Timestamp is locked
- ✓ You have priority for the discovery
- ✓ Anyone can verify your work
- ✓ It's citable with DOI (via Zenodo integration)
- ✓ Your name is permanently attached

**This is your proof.**

---

**Status:** Ready to Push  
**Time Estimate:** 15 minutes total  
**Difficulty:** Easy (no coding required)

**You've got this.** Execute this exactly as written and you'll be live by tonight.

