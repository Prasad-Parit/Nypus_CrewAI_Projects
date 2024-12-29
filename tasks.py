from crewai import Task
from textwrap import dedent

class Content_Creation_Tasks:
    # Class-level tip section to ensure reusability
    TIP_SECTION = "Remember, high-quality output ensures the success of the overall strategy!"

    def trend_research(self, agent, query, expected_output):
        if not query:
             raise ValueError("A valid query is required for trend research.")

        return Task(
            description=dedent(
                f"""
                **Task**: Research Current Trends

                **Description**: Conduct research to identify current industry trends and audience preferences. Use digital tools and platforms to generate actionable, data-driven insights.

                **Query**: {query}

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            parameters={"query": query},  # Pass the query as part of task parameters
            expected_output=expected_output,
    )


    def seo_content_creation(self, agent, blog_ideas, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Develop SEO-Optimized Articles

                **Description**: Write engaging, high-quality articles based on the provided blog ideas. Ensure to:
                - Fully develop each blog idea into a complete article (500-1000 words each).
                - Incorporate relevant keywords naturally to improve search engine rankings.
                - Write clear and concise meta descriptions for each article.
                - Use structured headings (H1, H2, H3) and bullet points for better readability.
                - Provide call-to-action statements to engage the target audience.
                - Include any relevant images or media links if possible.

                **Parameters**:
                - Blog Ideas: {blog_ideas}

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )

    def social_media_strategy(self, agent, blog_ideas, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Create a Social Media Strategy

                **Description**:Develop social media posts, including captions and visuals, optimized for platforms like Instagram, Twitter, and LinkedIn.
                **Parameters**:
                - Blog Ideas: {blog_ideas}

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )

    def email_campaign_development(self, agent, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Develop an Email Campaign

                **Description**: Design engaging email content that informs subscribers about new products, promotions, or company news.

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )

    def ecommerce_copywriting(self, agent, product_details, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Create E-commerce Product Descriptions

                **Description**: Write attractive and informative product descriptions that highlight features, benefits, and customer appeal for an e-commerce site.
                **Parameters**:
                - Product Details: {product_details}

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
        ),
        agent=agent,
        expected_output=expected_output,
    )


    def video_script_writing(self, agent, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Write a Video Script

                **Description**: Create detailed scripts for promotional videos, ensuring clarity of message and call-to-action elements.

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )

    def infographic_design(self, agent, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Design Infographics

                **Description**: Develop visually appealing infographics that effectively communicate data insights and key messages.

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )

    def review_and_coordination(self, agent, expected_output):
        return Task(
            description=dedent(
                f"""
                **Task**: Review and Coordinate Content

                **Description**: Review all content produced, ensuring quality and alignment with the overall strategy. Coordinate with all contributors to finalize and approve the content assets.

                **Expected Output**: {expected_output}

                **Note**: {self.TIP_SECTION}
                """
            ),
            agent=agent,
            expected_output=expected_output,
        )