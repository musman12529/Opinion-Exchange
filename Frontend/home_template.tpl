<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Forum Home</title>
</head>

<body>
    <header>
        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/mydrafts">My Drafts</a></li>
                <li><a href="/">Logout</a></li>
                <li><a href="/settings">Settings</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Welcome to the Forum</h1>
        
        <div class="search-bar">
            <input type="text" id="searchInput" placeholder="Search drafts by topic or author..." />
            <form action="">
                <select name="selectedTeam" id="" onchange="this.form.submit()">
                    <option value="0" 
                    % if 0 == selectedTeam:
                        selected="true"
                    % end
                    >Global</option>
                    % for team in teams:
                        <option value="{{team['id']}}" 
                        % if team['id'] == selectedTeam:
                            selected="true"
                        % end
                        >{{team['name']}}</option>
                    % end
                </select>
            </form>
        </div>
        <form action="/create-draft" method="post" class="draft-form">
            <label for="topic">Topic:</label>
            <input type="text" id="topic" name="topic" required><br>

            <label for="body">Body:</label>
            <textarea id="body" name="body" rows="4" required></textarea><br>
            <div style="display: flex; align-items: center;">
                <label style="margin: 0;" for="draft">Save as draft?</label>
                <input type="checkbox" name="draft">
            </div>
            <div style="display: flex; align-items: center;">
                <label style="margin: 0;" for="anonymous">Make anonymous?</label>
                <input type="checkbox" name="anonymous">
            </div>
            <br>
            <input type="number" name="team_id" value="{{selectedTeam}}" hidden>
            <button type="submit">Submit</button>
        </form>
        <div id="container">
            % for review in reviews:
            
            <div class="post">
                
                <h2><a href="/post/${data[i]['getID']}">{{review.get_topic()}}</a></h2>
                <div class="author" style="display: flex; align-items: center; gap: 10px;">
                    <img
                        width="40px"
                        src="https://api.dicebear.com/7.x/bottts-neutral/svg?seed={{review.get_author()['id']}}"
                        alt="avatar"
                    />
                    {{review.get_author()["username"]}}

                </div>
                <p>{{review.get_body()}}</p>
                <p>Average ratings:</p>
                <div>
                    <b>Technical Competence:</b> <br>
                    % for item in range(int(average_criterias[reviews.index(review)][0])):
                        ⭐
                    % end
                    <br>
                    <b>Collaboration and Communication:</b> <br>
                    % for item in range(int(average_criterias[reviews.index(review)][1])):
                        ⭐
                    % end
                    <br>
                    <b>Adaptability and Learning Ability:</b> <br>
                    % for item in range(int(average_criterias[reviews.index(review)][2])):
                        ⭐
                    % end
                    <br>
                    <b>Responsibility and Accountability:</b> <br>
                    % for item in range(int(average_criterias[reviews.index(review)][3])):
                        ⭐
                    % end
                    <br>
                    <b>Initiative and Proactiveness:</b> <br>
                    % for item in range(int(average_criterias[reviews.index(review)][4])):
                        ⭐
                    % end
                    <br>
                </div>
                <details class="comments">
                    <summary style="margin:20px 0">Comments</summary>

                    % for comment in review.get_comments():
                    <div class="comment" style="display: flex; flex-direction: column; gap: 5px; margin: 5px 0;">
                        <div class="user" style="display: flex; align-items: center; gap: 5px;">
                            <img
                                width="30px"
                                src="https://api.dicebear.com/7.x/bottts-neutral/svg?seed={{comment.get_author()['id']}}"
                                alt="avatar"
                            />
                            <strong>{{comment.get_author()["username"]}}</strong>
                        </div>
                        <div class="body">
                            <div style="margin: 10px 0;">{{comment.get_body()}}</div>
                            <div>
                                <b>Technical Competence:</b> <br>
                                % for item in range(comment.get_ratings().get_critA()):
                                    ⭐
                                % end
                                <br>
                                <b>Collaboration and Communication:</b> <br>
                                % for item in range(comment.get_ratings().get_critB()):
                                    ⭐
                                % end
                                <br>
                                <b>Adaptability and Learning Ability:</b> <br>
                                % for item in range(comment.get_ratings().get_critC()):
                                    ⭐
                                % end
                                <br>
                                <b>Responsibility and Accountability:</b> <br>
                                % for item in range(comment.get_ratings().get_critD()):
                                    ⭐
                                % end
                                <br>
                                <b>Initiative and Proactiveness:</b> <br>
                                % for item in range(comment.get_ratings().get_critE()):
                                    ⭐
                                % end
                                <br>
                            </div>
                        </div>
                    </div>
                    %end
                </details>
                <form action="/create-comment" method="POST" style="margin: 10px 0;">
                    <input type="number" name="review_id" id="" hidden value="{{review.get_id()}}">
                    <textarea name="comment" type="text" placeholder="Write a comment"></textarea>
                    <label for="criteria1" class="rating-label">Technical Competence</label>
                    <input type="range" name="criteria1" id="" class="rating" max="5" oninput="this.style.setProperty('--value', this.value)">
                    <label for="criteria2" class="rating-label">Collaboration and Communication</label>
                    <input type="range" name="criteria2" id="" class="rating" max="5" oninput="this.style.setProperty('--value', this.value)">
                    <label for="criteria3" class="rating-label">Adaptability and Learning Ability</label>
                    <input type="range" name="criteria3" id="" class="rating" max="5" oninput="this.style.setProperty('--value', this.value)">
                    <label for="criteria4" class="rating-label">Responsibility and Accountability</label>
                    <input type="range" name="criteria4" id="" class="rating" max="5" oninput="this.style.setProperty('--value', this.value)">
                    <label for="criteria5" class="rating-label">Initiative and Proactiveness</label>
                    <input type="range" name="criteria5" id="" class="rating" max="5" oninput="this.style.setProperty('--value', this.value)">
                    <button type="submit">Submit</button>
                </form>
            </div>

            % end
        </div>
        <!-- # Clinton Sprint 3 code -->
        <form action="/addUserToTeam" method="post" class="draft-form">
            <label for="username">User to add:</label>
            <input type="text" id="username" name="username" placeholder="Enter username">
            <input type="number" name="team_id" value="{{selectedTeam}}" hidden>
            <button type="submit">Add User to Team</button>
        </form>
        <!-- end -->
    </main>

    <script>


        const searchInput = document.getElementById("searchInput");
        searchInput.addEventListener("input", function () {
            const searchTerm = searchInput.value.toLowerCase();
            const allDrafts = document.querySelectorAll(".post");
            allDrafts.forEach((draft) => {
                const topic = draft.querySelector("h2 a").textContent.toLowerCase();
                const author = draft.querySelector("p").textContent.toLowerCase();
                if (topic.includes(searchTerm) || author.includes(searchTerm)) {
                    draft.style.display = "block";
                } else {
                    draft.style.display = "none";
                }
            });
        });
    </script>
</body>

</html>