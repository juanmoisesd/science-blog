# 🧠 Multilingual Science Blog

A comprehensive multilingual blogging platform dedicated to **Psychology & Neuroscience** research and insights, supporting **37 languages** with automated content generation and deployment.

![Languages](https://img.shields.io/badge/Languages-37-blue)
![Status](https://img.shields.io/badge/Status-Active-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📚 Overview

This project generates static HTML websites from WordPress content, creating a multilingual science blog available in:

**European Languages:** English, Spanish, French, German, Italian, Portuguese, Dutch, Polish, Romanian, Czech, Hungarian, Swedish, Greek, Bulgarian, Danish, Finnish, Slovak, Croatian, Lithuanian, Latvian, Slovenian, Estonian, Irish, Maltese

**Asian Languages:** Russian, Chinese (Simplified), Hindi, Japanese, Hebrew, Indonesian, Bengali, Turkish, Korean, Vietnamese, Persian, Arabic

## 🎯 Features

- ✅ **37 Language Support** - Automatic generation for all supported languages
- - ✅ **SEO Optimized** - Meta tags, Open Graph, structured data (JSON-LD)
  - - ✅ **Responsive Design** - Mobile-friendly HTML templates
    - - ✅ **Static Site Generation** - Fast, secure, low-maintenance
      - - ✅ **Sitemap & Robots.txt** - Search engine friendly
        - - ✅ **GitHub Pages Ready** - Deploy directly from repository
          - - ✅ **Automated CI/CD** - GitHub Actions for continuous deployment
            - - ✅ **Scientific Content** - Psychology and Neuroscience focus
             
              - ## 🚀 Quick Start
             
              - ### Prerequisites
             
              - - Python 3.8+
                - - pip (Python package manager)
                  - - Git
                    - - GitHub Account
                     
                      - ### Installation
                     
                      - 1. **Clone the repository:**
                        2. ```bash
                           git clone https://github.com/juanmoisesd/science-blog.git
                           cd science-blog
                           ```

                           2. **Create virtual environment:**
                           3. ```bash
                              python -m venv venv
                              source venv/bin/activate  # On Windows: venv\Scripts\activate
                              ```

                              3. **Install dependencies:**
                              4. ```bash
                                 pip install -r requirements.txt
                                 ```

                                 4. **Configure environment variables:**
                                 5. ```bash
                                    cp .env.example .env
                                    # Edit .env with your WordPress credentials
                                    nano .env
                                    ```

                                    5. **Run the site generator:**
                                    6. ```bash
                                       python site_builder.py
                                       ```

                                       6. **View the generated site:**
                                       7. ```bash
                                          # Open index.html in your browser
                                          open index.html
                                          ```

                                          ## 📁 Project Structure

                                          ```
                                          science-blog/
                                          ├── README.md                 # Project documentation
                                          ├── requirements.txt          # Python dependencies
                                          ├── .env.example             # Environment variables template
                                          ├── .gitignore               # Git ignore rules
                                          ├── site_builder.py          # Main site generation script
                                          ├── index.html               # Root index (language selector)
                                          ├── robots.txt               # Search engine directives
                                          ├── sitemap.xml              # XML sitemap
                                          ├── .nojekyll                # GitHub Pages config
                                          │
                                          ├── [Language Folders] (37 total)
                                          │   ├── ara/                 # Arabic
                                          │   ├── ben/                 # Bengali
                                          │   ├── deu/                 # German
                                          │   ├── eng/                 # English
                                          │   ├── fra/                 # French
                                          │   ├── jpn/                 # Japanese
                                          │   ├── spa/                 # Spanish
                                          │   ├── zho/                 # Chinese (Simplified)
                                          │   └── ... (33 more)
                                          │
                                          └── raw_content/
                                              ├── posts.json           # WordPress posts backup
                                              └── pages.json           # WordPress pages backup
                                          ```

                                          ## 🔧 Configuration

                                          ### Environment Variables (.env)

                                          Create a `.env` file with the following variables:

                                          ```env
                                          # WordPress Configuration
                                          WP_BASE_URL=https://yourblog.com/wp-json/wp/v2
                                          WP_USERNAME=your_username
                                          WP_PASSWORD=your_password
                                          WP_AUTH_TYPE=basic

                                          # Site Configuration
                                          SITE_URL=https://yourusername.github.io/science-blog
                                          SITE_NAME=Science Blog
                                          SITE_DESCRIPTION=Psychology & Neuroscience Research

                                          # GitHub Configuration (optional for CI/CD)
                                          GITHUB_TOKEN=your_github_token
                                          GITHUB_REPO=yourusername/science-blog
                                          ```

                                          ### Supported Languages

                                          The script automatically generates content for all 37 supported languages:

                                          | Code | Language | RTL | Code | Language | RTL |
                                          |------|----------|-----|------|----------|-----|
                                          | eng | English | - | ara | Arabic | ✓ |
                                          | spa | Spanish | - | heb | Hebrew | ✓ |
                                          | fra | French | - | fas | Persian | ✓ |
                                          | deu | German | - | jpn | Japanese | - |
                                          | ita | Italian | - | zho | Chinese | - |
                                          | por | Portuguese | - | hin | Hindi | - |
                                          | nld | Dutch | - | ben | Bengali | - |
                                          | pol | Polish | - | kor | Korean | - |
                                          | rus | Russian | - | vie | Vietnamese | - |
                                          | ... | ... | ... | ... | ... | ... |

                                          ## 📝 Usage

                                          ### Generate Site from WordPress

                                          ```bash
                                          # Fetch content and generate all language versions
                                          python site_builder.py
                                          ```

                                          The script will:
                                          1. Fetch all posts and pages from WordPress
                                          2. 2. Save raw content to `raw_content/`
                                             3. 3. Generate individual article pages for each language
                                                4. 4. Create language-specific index pages
                                                   5. 5. Generate sitemap.xml and robots.txt
                                                     
                                                      6. ### Customize Content
                                                     
                                                      7. Edit `site_builder.py` to modify:
                                                      8. - Content templates
                                                         - - HTML styling
                                                           - - Language configurations
                                                             - - URL patterns
                                                               - - Metadata generation
                                                                
                                                                 - ## 🌐 Deployment
                                                                
                                                                 - ### GitHub Pages (Recommended)
                                                                
                                                                 - 1. **Enable GitHub Pages:**
                                                                   2.    - Go to Repository Settings → Pages
                                                                         -    - Select "Deploy from a branch"
                                                                              -    - Choose "main" branch and "root" directory
                                                                               
                                                                                   - 2. **Automatic Deployment:**
                                                                                     3.    - Push changes to main branch
                                                                                           -    - GitHub Pages automatically deploys static files
                                                                                                -    - Site is live at: `https://yourusername.github.io/science-blog/`
                                                                                                 
                                                                                                     - 3. **With GitHub Actions (CI/CD):**
                                                                                                       4.    - Repository automatically includes `.github/workflows/deploy.yml`
                                                                                                             -    - Triggers on push to main
                                                                                                                  -    - Runs site_builder.py automatically
                                                                                                                   
                                                                                                                       - ### Local Testing
                                                                                                                   
                                                                                                                       - ```bash
                                                                                                                         # Python's built-in server
                                                                                                                         python -m http.server 8000

                                                                                                                         # Visit: http://localhost:8000
                                                                                                                         ```
                                                                                                                         
                                                                                                                         ## 🔐 Security
                                                                                                                         
                                                                                                                         ⚠️ **IMPORTANT SECURITY NOTES:**
                                                                                                                         
                                                                                                                         1. **Never commit .env file** - Always use `.env.example` as template
                                                                                                                         2. 2. **Use environment variables** - Store credentials in `.env`, not in code
                                                                                                                            3. 3. **GitHub Secrets** - For CI/CD, use GitHub repository secrets
                                                                                                                               4. 4. **Rotate credentials** - Change WordPress password periodically
                                                                                                                                  5. 5. **Sanitize content** - BeautifulSoup automatically handles this
                                                                                                                                    
                                                                                                                                     6. ### Secure Workflow
                                                                                                                                    
                                                                                                                                     7. ```bash
                                                                                                                                        # 1. Create .env from example (never commit .env)
                                                                                                                                        cp .env.example .env

                                                                                                                                        # 2. Add credentials to .env
                                                                                                                                        echo "WP_PASSWORD=your_secure_password" >> .env

                                                                                                                                        # 3. .gitignore prevents accidental commits
                                                                                                                                        cat .gitignore | grep .env
                                                                                                                                        # Output: .env

                                                                                                                                        # 4. For GitHub Actions, use repository secrets
                                                                                                                                        # Settings → Secrets and variables → Actions
                                                                                                                                        # Add: WP_USERNAME, WP_PASSWORD, etc.
                                                                                                                                        ```
                                                                                                                                        
                                                                                                                                        ## 📊 Site Statistics
                                                                                                                                        
                                                                                                                                        - **Total Languages:** 37
                                                                                                                                        - - **Content Types:** Articles + Pages
                                                                                                                                          - - **Generated Files:** Dynamic (depends on WordPress content)
                                                                                                                                            - - **Site Size:** Typically 10-50MB (static HTML)
                                                                                                                                              - - **Build Time:** 2-5 minutes (depending on content volume)
                                                                                                                                               
                                                                                                                                                - ## 🛠️ Troubleshooting
                                                                                                                                               
                                                                                                                                                - ### Issue: WordPress Connection Failed
                                                                                                                                               
                                                                                                                                                - ```bash
                                                                                                                                                  # Check credentials in .env
                                                                                                                                                  cat .env

                                                                                                                                                  # Verify WordPress endpoint
                                                                                                                                                  curl -u username:password https://yourblog.com/wp-json/wp/v2/posts
                                                                                                                                                  ```
                                                                                                                                                  
                                                                                                                                                  ### Issue: Missing Dependencies
                                                                                                                                                  
                                                                                                                                                  ```bash
                                                                                                                                                  # Reinstall all requirements
                                                                                                                                                  pip install --upgrade -r requirements.txt
                                                                                                                                                  ```
                                                                                                                                                  
                                                                                                                                                  ### Issue: Permission Errors
                                                                                                                                                  
                                                                                                                                                  ```bash
                                                                                                                                                  # On Linux/Mac, ensure script is executable
                                                                                                                                                  chmod +x site_builder.py
                                                                                                                                                  python site_builder.py

                                                                                                                                                  # Or use explicit Python call
                                                                                                                                                  python3 site_builder.py
                                                                                                                                                  ```
                                                                                                                                                  
                                                                                                                                                  ### Issue: Special Characters Display Incorrectly
                                                                                                                                                  
                                                                                                                                                  - Ensure UTF-8 encoding: `export PYTHONIOENCODING=utf-8`
                                                                                                                                                  - - Check WordPress content encoding
                                                                                                                                                    - - Verify HTML meta charset: `<meta charset="UTF-8">`
                                                                                                                                                    
                                                                                                                                                    ## 📚 Content Guidelines
                                                                                                                                                    
                                                                                                                                                    ### Article Structure
                                                                                                                                                    
                                                                                                                                                    Each generated article includes:
                                                                                                                                                    1. **Title** - Translated/localized
                                                                                                                                                    2. 2. **Meta Description** - SEO optimized
                                                                                                                                                       3. 3. **Keywords** - Relevant to psychology/neuroscience
                                                                                                                                                          4. 4. **TL;DR** - Quick summary points
                                                                                                                                                             5. 5. **Table of Contents** - Auto-generated from headings
                                                                                                                                                                6. 6. **Content** - Main article body
                                                                                                                                                                   7. 7. **Related Articles** - Linked articles
                                                                                                                                                                      8. 8. **Structured Data** - JSON-LD schema
                                                                                                                                                                        
                                                                                                                                                                         9. ### Best Practices
                                                                                                                                                                         
                                                                                                                                                                         - Write scientifically accurate content
                                                                                                                                                                         - Use clear, accessible language
                                                                                                                                                                         - - Include recent research (2024+)
                                                                                                                                                                           - - Add relevant links and citations
                                                                                                                                                                             - - Optimize for mobile reading
                                                                                                                                                                             - Include multimedia (images, diagrams)
                                                                                                                                                                             
                                                                                                                                                                             ## 🤝 Contributing
                                                                                                                                                                             
                                                                                                                                                                             Contributions are welcome! 
                                                                                                                                                                             
                                                                                                                                                                             1. Fork the repository
                                                                                                                                                                             2. 2. Create a feature branch: `git checkout -b feature/your-feature`
                                                                                                                                                                                3. 3. Commit changes: `git commit -m 'Add new feature'`
                                                                                                                                                                                4. Push to branch: `git push origin feature/your-feature`
                                                                                                                                                                                5. Open a Pull Request
                                                                                                                                                                                
                                                                                                                                                                                ### Areas for Contribution
                                                                                                                                                                                
                                                                                                                                                                                - [ ] Add more languages
                                                                                                                                                                                - [ ] Improve CSS styling
                                                                                                                                                                                - [ ] Add dark mode
                                                                                                                                                                                - [ ] Enhance mobile responsiveness
                                                                                                                                                                                - [ ] Create language-specific themes
                                                                                                                                                                                - [ ] Add search functionality
                                                                                                                                                                                - [ ] - [ ] Improve content templates
                                                                                                                                                                                
                                                                                                                                                                                ## 📄 License
                                                                                                                                                                                
                                                                                                                                                                                This project is licensed under the **MIT License** - see the LICENSE file for details.
                                                                                                                                                                                
                                                                                                                                                                                ## 👨‍💻 Author
                                                                                                                                                                                
                                                                                                                                                                                **Juan Moisés de la Serna**
                                                                                                                                                                                - Website: [https://juanmoisesdelaserna.es](https://juanmoisesdelaserna.es)
                                                                                                                                                                                - GitHub: [@juanmoisesd](https://github.com/juanmoisesd)
                                                                                                                                                                                - Research Focus: Psychology & Neuroscience
                                                                                                                                                                                
                                                                                                                                                                                ## 📞 Support
                                                                                                                                                                                
                                                                                                                                                                                - 📧 Email: jmsernatuya@gmail.com
                                                                                                                                                                                - - 🐛 Issues: [GitHub Issues](https://github.com/juanmoisesd/science-blog/issues)
                                                                                                                                                                                  - - 💬 Discussions: [GitHub Discussions](https://github.com/juanmoisesd/science-blog/discussions)
                                                                                                                                                                                  
                                                                                                                                                                                  ## 🔗 Related Resources
                                                                                                                                                                                  
                                                                                                                                                                                  - [WordPress REST API Documentation](https://developer.wordpress.org/rest-api/)
                                                                                                                                                                                  - [Jinja2 Template Engine](https://jinja.palletsprojects.com/)
                                                                                                                                                                                  - [GitHub Pages Documentation](https://pages.github.com/)
                                                                                                                                                                                  - [HTML5 Semantic Web](https://www.w3.org/TR/html52/)
                                                                                                                                                                                  - [Psychology Research Databases](https://www.apa.org/science/about/psa/research-resources)
                                                                                                                                                                                  
                                                                                                                                                                                  ## 📈 Roadmap
                                                                                                                                                                                  
                                                                                                                                                                                  - [ ] API endpoint for dynamic content
                                                                                                                                                                                  - [ ] Full-text search functionality
                                                                                                                                                                                  - [ ] User comments system
                                                                                                                                                                                  - [ ] Category/tag organization
                                                                                                                                                                                  - [ ] Author profiles
                                                                                                                                                                                  - [ ] Newsletter subscription
                                                                                                                                                                                  - [ ] Social media integration
                                                                                                                                                                                  - [ ] Analytics dashboard
                                                                                                                                                                                  
                                                                                                                                                                                  ## 🙏 Acknowledgments
                                                                                                                                                                                  
                                                                                                                                                                                  Special thanks to:
                                                                                                                                                                                  - WordPress REST API team
                                                                                                                                                                                  - Jinja2 template developers
                                                                                                                                                                                  - BeautifulSoup community
                                                                                                                                                                                  - GitHub Pages infrastructure
                                                                                                                                                                                  - All science writers and researchers
                                                                                                                                                                                  
                                                                                                                                                                                  ---
                                                                                                                                                                                  
                                                                                                                                                                                  **Last Updated:** April 4, 2026  
                                                                                                                                                                                  **Status:** Active Development  
                                                                                                                                                                                  **Version:** 1.0.0

## How to Cite

If you use this repository in your research, please cite:

> de la Serna, J. M. (2026). *Science Blog*. Universidad Internacional de La Rioja (UNIR).
> https://github.com/juanmoisesd/science-blog 

See `CITATION.cff` for formatted references.
