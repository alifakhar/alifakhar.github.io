---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

# Master Thesis:
## ABSTRACT
Graph signals are sets of values residing on sets of nodes that are connected via edges. Graph Neural Networks (GNNs) are a type of machine learning model for working with graph-structured data, such as graph signals. GNNs have applications in graph classification, node classification, and link prediction. They can be thought of as learnable filters.

In this thesis, our focus is on graph filters and enhancing the performance of GNNs. In the first part, we aim to reduce computational costs in graph signal processing, particularly in graph filters. We explore methods to transform signals to the frequency domain with lower computational cost. In the latter part, we examine regulations in detail. Dropout and node dropout are common tools used to address the problem of overgeneralization. However, these tools do not consider the structure of the graph during the learning process.

For the first time, we propose using structure-based dropout in GNNs. Through numerical simulations in the task of node classification, we confirm that our proposed regularization method (Structure-based dropout) increases the accuracy of the network over using dropout.