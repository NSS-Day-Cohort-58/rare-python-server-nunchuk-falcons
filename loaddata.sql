CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO posts ('user_id', 'category_id', 'title', 'publication_date',
    'image_url', 'content', 'approved') VALUES (1, 2, 'Test Title', '2022-10-15',
    '', 'Test content', 1) 

INSERT INTO PostTags ('post_id', 'tag_id') VALUES (1, 2)

INSERT INTO Posts ('user_id', 'category_id', 'title','publication_date', 'image_url', 'content', 'approved')
VALUES ( 2, 3, 'Life in Peaces', '2022-10-02', 'www.getbehind.com', 'Text', True);
INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Sports');
INSERT INTO Categories ('label') VALUES ('Family');
INSERT INTO Categories ('label') VALUES ('Love');
INSERT INTO Categories ('label') VALUES ('Travel');
INSERT INTO Categories ('label') VALUES ('Jobs');
INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Tags ('label') VALUES ('Money');
INSERT INTO Tags ('label') VALUES ('Relationship');
INSERT INTO Tags ('label') VALUES ('Foodie');
INSERT INTO Tags ('label') VALUES ('Football');
INSERT INTO Tags ('label') VALUES ('Python');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Posts ('user_id', 'category_id', 'title','publication_date', 'image_url', 'content', 'approved') 
VALUES ( 2, 3, 'Life in Peaces', '2022-10-02', 'www.getbehind.com', 'Text', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title','publication_date', 'image_url', 'content', 'approved') 
VALUES ( 2, 3, 'The Inner Game of Tennis', '2022-10-04', 'www.innergame.com', 'book', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title','publication_date', 'image_url', 'content', 'approved') 
VALUES ( 2, 3, 'The Alchemist', '2022-09-02', 'www.alchemy.com', 'book', 1);
INSERT INTO Posts ('user_id', 'category_id', 'title','publication_date', 'image_url', 'content', 'approved') 
VALUES ( 2, 3, 'Great Big World', '2022-10-22', 'www.bigole.com', 'book', 1);

INSERT INTO Users ('id', 'first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active')
VALUES (5, 'Bilbo', 'Baggins', 'hairyfeet@gmail.com', 'Just a simple Hobbit who loves cake', 'bbaggins', '12345', null, '101026', 'active')

