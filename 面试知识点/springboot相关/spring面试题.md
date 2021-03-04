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
    MVC - 对 web 应用提供了高 度可配置性，其他框架的集成也十分方便。事务管理 - 提供了用于事务管理的通用抽象层。Spring 的事务支持也可用于容器较少的环境。
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


用过 Spring 框架的都知道 Spring 能流行是因为它的两把利器：IOC 和 AOP，
IOC 可以帮助我们管理对象的依赖关系，极大减少对象的耦合性，
而 AOP 的切面编程功能可以更方面的使用动态代理来实现各种动态方法功能（如事务、缓存、日志等）。

#springboot与传统spring项目简单区别
Spring Boot是在Spring的基础上面搭设的框架，目的是为了简化Spring项目的搭设和开发过程。

旧时我们开发一个普通spring的项目时,会存在很难麻烦的xml配置过程
    准备相关jar包依赖,包括spring、springmvc、redis、mybaits、log4j、mysql-connector-java 等等相关jar ...
    配置web.xml文件,Listener配置, Filter配置,servlet配置,log4j配置, error配置...
    配置数据库链接,配置spring事务
    配置视图解析器
    开启注解,自动扫描功能
    配置完成后, 部署tomcat,启动调试
    
现在,有了springboot,大大减少配置时间,一键启动, 方便又快捷
    起步依赖
    配置数据源
    创建入口 @SpringBootApplication

# 拦截器和过滤器区别
　　①拦截器是基于java的反射机制的，而过滤器是基于函数回调。
　　②拦截器不依赖与servlet容器，过滤器依赖与servlet容器。
　　③拦截器只能对action请求起作用，而过滤器则可以对几乎所有的请求起作用。
　　④拦截器可以访问action上下文、值栈里的对象，而过滤器不能访问。
　　⑤在action的生命周期中，拦截器可以多次被调用，而过滤器只能在容器初始化时被调用一次。
　　⑥拦截器可以获取IOC容器中的各个bean，而过滤器就不行，这点很重要，在拦截器里注入一个service，可以调用业务逻辑。