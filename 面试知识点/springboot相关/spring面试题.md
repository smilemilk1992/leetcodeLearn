1、什么是 Spring Framework
    
    Spring 是一个开源应用框架，旨在降低应用程序开发的复杂度。
    它是轻量级、松 散耦合的。它具有分层体系结构，允许用户选择组件，同时还为 J2EE 应用程序 开发提供了一个有凝聚力的框架。
    它可以集成其他框架，如 Structs、Hibernate、 EJB 等，所以又称为框架的框架。

2、列举 Spring Framework 的优点。
    
    由于 Spring Frameworks 的分层架构，用户可以自由选择自己需要的组件。 
    Spring Framework 支持 POJO(Plain Old Java Object) 编程，从而具备持续集 成和可测试性。
    由于依赖注入和控制反转，JDBC 得以简化。它是开源免费的。

3、Spring Framework 有哪些不同的功能？
    
    轻量级 - Spring 在代码量和透明度方面都很轻便。
    IOC - 控制反转 
    AOP - 面向 切面编程可以将应用业务逻辑和系统服务分离，以实现高内聚。
    容器 - Spring 负 责创建和管理对象（Bean）的生命周期和配置。
    MVC - 对 web 应用提供了高 度可配置性，其他框架的集成也十分方便。事务管理 - 提供了用于事务管理的通 用抽象层。Spring 的事务支持也可用于容器较少的环境。
    JDBC 异常 - Spring 的 JDBC 抽象层提供了一个异常层次结构，简化了错误处理策略。

4、SpringFramework 中有多少个模块，它们分别是什么？
    
    Spring 核心容器 – 该层基本上是 Spring Framework 的核心。它包含以下模 块：
         Spring Core 
         Spring Bean 
         SpEL (Spring Expression Language) 
         Spring Context

    数据访问/集成 – 该层提供与数据库交互的支持。它包含以下模块：
         JDBC (Java DataBase Connectivity) 
         ORM (Object Relational Mapping) 
         OXM (Object XML Mappers)
         JMS (Java Messaging Service) 
         Transaction
    
    Web – 该层提供了创建 Web 应用程序的支持。它包含以下模块：
         Web 
         Web – Servlet 
         Web – Socket 
         Web – Portlet
    AOP - 该层支持面向切面编程
    Instrumentation - 该层为类检测和类加载器实现提供支持
    Test - 该层为使用 JUnit 和 TestNG 进行测试提供支持。
    Messaging – 该模块为 STOMP 提供支持。它还支持注解编程模型，该模型用 于从 WebSocket 客户端路由和处理 STOMP 消息。
    Aspects – 该模块为与 AspectJ 的集成提供支持。


5、什么是依赖注入

    在依赖注入中，您不必创建对象，但必须描述如何创建它们。
    您不是直接在代码 中将组件和服务连接在一起，而是描述配置文件中哪些组件需要哪些服务。
    由 IoC 容器将它们装配在一起。

6、可以有多少种方式完成依赖注入
    
    通常，依赖注入可以通过三种方式完成，即：
         构造函数注入 
         setter 注入 
         接口注入
    在 Spring Framework 中，仅使用构造函数和 setter 注入。


