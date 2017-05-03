import fresh_tomatoes
import movie
#creating Toy Story object
toy_story = movie.Movie("Toy Story",
                        "A story of a boy and his toys that come to live",
                        "http://vignette4.wikia.nocookie.net/disney/images"\
                        "/4/4c/"\
                        "Toy-story-movie-posters-4.jpg/"
                        "revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")


#creating Transformers object
transformers = movie.Movie("Transformers",
                           "The fate of humanity is at stake when two races"\
                           "of robots,the good Autobots and the villainous"\
                           "Decepticons,bring their"\
                           "war to Earth. The robots have the"\
                           "ability to change into different mechanical"\
                           "objects"
                           "as they seek the key to ultimate power. Only a"
                           "human youth, Sam Witwicky (Shia LaBeouf)"\
                           "can save the world from total destruction.",
                           "http://www.gstatic.com/tv/thumb/movieposters"
                           "/159729/p159729_p_v8_aq.jpg",
                           "https://www.youtube.com/watch?v=KrUhwet0ngg")

#creating Stomp The Yard object
stomp_the_yard = movie.Movie("Stomp The Yard",
                             "After his brother's death, a troubled but gifted"
                             "street dancer enrolls in Atlanta's Truth"
                             "University.As he tries to concentrate"
                             "on his studies and woo a pretty"
                             "classmate, he finds himself in the middle"\
                             "of a tug-of-war between fraternities, who want"
                             "to utilize his talents in an upcoming"
                             "dance competition.",
                             "http://www.gstatic.com/tv/thumb/dvdboxart/"
                             "162827/p162827_d_v8_aa.jpg",
                             "https://www.youtube.com/watch?v=hvLzhK7Vatw")
#creating Get Out object
get_out = movie.Movie("Get Out",
                    "Now that Chris (Daniel Kaluuya) and his girlfriend, Rose"
                    "(Allison Williams), have reached the meet-the-parents"\
                    "milestone of dating, she invites him for a weekend"
                    "getaway upstate with Missy and Dean. At first, Chris"
                    "reads the family's overly accommodating behavior"
                    "as nervous attempts to deal with their daughter's"
                    "interracial relationship,but as the weekend progresses"
                    ", a series of increasingly disturbing discoveries"
                    "lead him to a truth that he never could have imagined.",
                    "https://cdn.traileraddict.com/content/universal-pictures/"
                    "get-out-2017-2.jpg",
                    "https://www.youtube.com/watch?v=A2JbO9lnVLE")

#creating The Accountant object
the_accountant = movie.Movie("The Accountant",
                           "Christian Wolff (Ben Affleck) is a mathematics"
                           "savant with more affinity for numbers"
                           "than people.Using a small-town CPA office"
                           "as a cover, he makes his"
                           "living as a freelance accountant for dangerous"\
                           "criminal organizations. With a Treasury agent"
                           "(J.K. Simmons) hot on his heels,"
                           "Christian takes on a"\
                           "state-of-the-art robotics company"
                           "as a legitimate client"
                           ". As Wolff gets closer to the truth about a"\
                           "discrepancy that involves millions of dollars,"
                           "the body count starts to rise.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcS"
                           "TfMmvT_-0ELHJlI6OrXOoPCZqV6hlty_A6mvaABzaJRkoBgzW",
                           "https://www.youtube.com/watch?v=DBfsgcswlYQ")

#creating guardians of the galaxy object
guardians_of_the_galaxy = movie.Movie("Guardians of the Galaxy",
                           "Brash space adventurer Peter Quill (Chris Pratt)"
                           "finds himself the quarry of relentless bounty"
                           "hunters"\
                           "after he steals an orb coveted by Ronan, a"
                           "powerful villain. To evade Ronan, Quill is"
                           "forced into an uneasy truce with four disparate"
                           "misfits: gun-toting Rocket Raccoon,"
                           "treelike-humanoid Groot,"\
                           "enigmatic Gamora, and vengeance-driven"
                           "Drax the Destroyer."
                           "But when he discovers the orb's true"\
                           "power and the cosmic threat it poses, Quill must"
                           "rally his ragtag group to save the universe.",
                           "https://lh3.googleusercontent.com/-Glzj9zb8mRw/"
                           "VDr1bPJxtTI/AAAAAAAAAMA/0VmhS2IK1Wc05tz"
                           "gu4HoCN_pPROOkZcogCJoC/"
                           "w800-h800/10672330_67188876625"
                           "9482_6844791399166584697_n.jpg",
                           "https://www.youtube.com/watch?v=d96cjJhvlMA")
#make list of favorite movies
movies = [toy_story, transformers, stomp_the_yard, get_out,\
         the_accountant, guardians_of_the_galaxy]
#pass list of favorite movies to open_movies_page
#function defined in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
